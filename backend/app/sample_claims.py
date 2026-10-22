from __future__ import annotations

import sqlite3
import uuid
from pathlib import Path
from typing import Any, Dict

from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from backend.app.logic import verify_claim

BASE_DIR = Path(__file__).resolve().parent.parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"
DB_PATH = BASE_DIR / "data" / "unmai_results.db"

DB_PATH.parent.mkdir(parents=True, exist_ok=True)

app = FastAPI(title="UNMAI", version="0.1.0")


class TextVerifyRequest(BaseModel):
    claim: str = Field(..., min_length=1)
    region: str = "global"


class ResultPayload(BaseModel):
    result: Dict[str, Any]


def init_db() -> None:
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS results (
                result_id TEXT PRIMARY KEY,
                created_at TEXT NOT NULL,
                region TEXT,
                status TEXT,
                claim TEXT,
                explanation TEXT,
                confidence REAL,
                result_json TEXT
            )
            """
        )
        conn.commit()


@app.on_event("startup")
def startup_event() -> None:
    init_db()


@app.get("/")
def index() -> FileResponse:
    return FileResponse(FRONTEND_DIR / "index.html")


app.mount("/static", StaticFiles(directory=str(FRONTEND_DIR)), name="static")


@app.get("/api/health")
def health() -> dict:
    return {"status": "ok", "service": "UNMAI"}


@app.get("/api/test-data")
def test_data() -> dict:
    return {
        "examples": [
            "The Earth is round.",
            "The Moon landing was faked.",
            "COVID-19 vaccines are safe and effective.",
            "India launched Chandrayaan-3 in 2023.",
            "A local flood warning was issued by the state government.",
        ]
    }


@app.post("/api/verify/text")
def verify_text(payload: TextVerifyRequest) -> dict:
    result = verify_claim(payload.claim, region=payload.region)
    return result


@app.post("/api/verify/image")
async def verify_image(file: UploadFile = File(...), region: str = Form("global")) -> dict:
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file selected.")

    allowed = {"png", "jpg", "jpeg", "webp"}
    suffix = (file.filename or "").split(".")[-1].lower()
    if suffix not in allowed:
        raise HTTPException(status_code=400, detail="Unsupported file type. Upload a JPG, PNG, or WebP image.")

    try:
        from PIL import Image
        import pytesseract
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Image processing dependencies are missing: {exc}")

    try:
        contents = await file.read()
        image = Image.open(__import__("io").BytesIO(contents)).convert("RGB")
        try:
            extracted_text = pytesseract.image_to_string(image)
        except Exception:
            extracted_text = "Image uploaded successfully but OCR could not read text from the file."

        cleaned_text = extracted_text.strip() or "Image uploaded successfully but OCR did not extract readable text."
        result = verify_claim(cleaned_text, region=region)
        result["image_note"] = "OCR text extracted from the uploaded image and assessed using the same evidence-based workflow."
        result["ocr_text"] = cleaned_text[:4000]
        return result
    except Exception as exc:
        raise HTTPException(status_code=400, detail=f"Could not process the image: {exc}")


@app.post("/api/results")
def create_result(payload: ResultPayload) -> dict:
    result = payload.result
    result_id = str(uuid.uuid4())
    created_at = __import__("datetime").datetime.utcnow().isoformat() + "Z"

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO results (result_id, created_at, region, status, claim, explanation, confidence, result_json) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (
                result_id,
                created_at,
                result.get("region", "global"),
                result.get("status", "Unverified"),
                result.get("claim", ""),
                result.get("explanation", ""),
                result.get("confidence", 0.0),
                __import__("json").dumps(result),
            ),
        )
        conn.commit()

    return {"result_id": result_id, "created_at": created_at, "status": result.get("status", "Unverified")}


@app.get("/api/results/{result_id}")
def get_result(result_id: str) -> dict:
    with sqlite3.connect(DB_PATH) as conn:
        row = conn.execute(
            "SELECT result_id, created_at, region, status, claim, explanation, confidence, result_json FROM results WHERE result_id = ?",
            (result_id,),
        ).fetchone()

    if not row:
        raise HTTPException(status_code=404, detail="Result not found.")

    return {
        "result_id": row[0],
        "created_at": row[1],
        "region": row[2],
        "status": row[3],
        "claim": row[4],
        "explanation": row[5],
        "confidence": row[6],
        "result": __import__("json").loads(row[7]),
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("backend.app.main:app", host="0.0.0.0", port=8000, reload=True)
