# UNMAI

UNMAI is an AI-assisted fact-checking prototype for text and image claims. It helps users check whether a claim is likely true, likely false, misleading, or unverified using a transparent evidence-based workflow.

## Features

- Text verification with claim extraction and evidence scoring
- Image verification with OCR and text extraction
- Region-aware evidence selection for local and international sources
- Result cards with status, confidence, explanation, supporting evidence, and source links
- Copy and share functionality for mobile-friendly verification
- SQLite-backed result storage for demo sharing

## Tech stack

- Backend: FastAPI, Pydantic, SQLite
- Frontend: HTML, CSS, JavaScript
- OCR: Tesseract via pytesseract
- Image processing: Pillow
- Testing: pytest

## Project structure

- `backend/app/main.py` – FastAPI entry point and API routes
- `backend/app/logic.py` – claim extraction, evidence selection, verdict logic
- `backend/app/sample_claims.py` – sample dataset for testing
- `frontend/` – static frontend files
- `tests/` – API tests

## Setup

1. Create and activate a virtual environment:

   python -m venv .venv
   source .venv/bin/activate

2. Install dependencies:

   pip install -r requirements.txt

3. Start the backend:

   uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000

4. Open the app in a browser:

   http://localhost:8000/

## API endpoints

- `GET /api/health`
- `GET /api/test-data`
- `POST /api/verify/text`
- `POST /api/verify/image`
- `POST /api/results`
- `GET /api/results/{result_id}`

## Region-aware verification

The app supports a simple geography-aware evidence model:

- `india` -> local sources like PIB, India government releases, and credible Indian coverage
- `global` -> international sources like WHO, Reuters, AP, and major institutions
- `us` -> US government and major news sources
- `other` -> general global sources with a neutral verification stance

This allows the prototype to prefer locally relevant evidence while still staying grounded in internationally trusted sources.

## Important notes

- UNMAI is an evidence-based assistant, not a guarantee of absolute truth.
- It does not use AI confidence alone as proof.
- If there is insufficient evidence or conflicting sources, it returns `Unverified` or `Misleading` instead of pretending certainty.
- For production use, connect the app to live search and fact-checking APIs with proper source validation and privacy controls.

## Sample test claims

- "The Earth is round."
- "The Moon landing was faked."
- "COVID-19 vaccines are safe and effective."
- "India launched Chandrayaan-3 in 2023."

## License

MIT
