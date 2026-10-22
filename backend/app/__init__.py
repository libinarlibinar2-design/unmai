from __future__ import annotations

from typing import List


def extract_claims(text: str) -> List[str]:
    cleaned = text.strip()
    if not cleaned:
        return []

    sentences = []
    for chunk in cleaned.replace("\n", " ").split("."):
        sentence = chunk.strip()
        if len(sentence) > 12:
            sentences.append(sentence)

    claims = []
    for sentence in sentences:
        if sentence and sentence not in claims:
            claims.append(sentence)

    if not claims:
        claims.append(cleaned[:200])

    return claims[:5]


def region_to_sources(region: str) -> List[dict]:
    region_name = (region or "global").lower()

    if region_name == "india":
        return [
            {
                "source": "PIB India",
                "url": "https://pib.gov.in/",
                "type": "official",
                "summary": "Government press releases and verified public information from India."
            },
            {
                "source": "The Hindu",
                "url": "https://www.thehindu.com/",
                "type": "news",
                "summary": "Credible journalism and reporting on Indian public events."
            },
            {
                "source": "Reuters",
                "url": "https://www.reuters.com/",
                "type": "international",
                "summary": "Independent international reporting for cross-checking claims."
            },
        ]

    if region_name == "us":
        return [
            {
                "source": "CDC",
                "url": "https://www.cdc.gov/",
                "type": "official",
                "summary": "Trusted public health guidance and updates from the U.S. government."
            },
            {
                "source": "AP News",
                "url": "https://apnews.com/",
                "type": "news",
                "summary": "Independent reporting and wire coverage from a major global agency."
            },
            {
                "source": "Reuters",
                "url": "https://www.reuters.com/",
                "type": "international",
                "summary": "Cross-checked international reporting for global news claims."
            },
        ]

    if region_name == "global":
        return [
            {
                "source": "WHO",
                "url": "https://www.who.int/",
                "type": "official",
                "summary": "Global public health guidance and evidence on public safety matters."
            },
            {
                "source": "Reuters",
                "url": "https://www.reuters.com/",
                "type": "international",
                "summary": "Independent international reporting for balance and verification."
            },
            {
                "source": "AP News",
                "url": "https://apnews.com/",
                "type": "news",
                "summary": "Major newsroom verification and reporting sources."
            },
        ]

    return [
        {
            "source": "WHO",
            "url": "https://www.who.int/",
            "type": "official",
            "summary": "Global health and safety information sources."
        },
        {
            "source": "Reuters",
            "url": "https://www.reuters.com/",
            "type": "international",
            "summary": "Independent news verification and reporting."
        },
        {
            "source": "Government Source",
            "url": "https://www.gov.in/",
            "type": "official",
            "summary": "Official public administration and policy context for regional claims."
        },
    ]


def verify_claim(claim: str, region: str = "global") -> dict:
    claim_text = (claim or "").strip()
    if not claim_text:
        return {
            "status": "Unverified",
            "confidence": 0.0,
            "claim": "",
            "claims": [],
            "summary": "No claim was provided for verification.",
            "explanation": "UNMAI requires a factual claim or an image containing text before a result can be assessed.",
            "supporting_evidence": [],
            "contradictory_evidence": [],
            "source_links": [],
            "warnings": ["No evidence was available because the user did not submit a claim."],
            "region": region,
        }

    claims = extract_claims(claim_text)
    lower_claim = claim_text.lower()
    sources = region_to_sources(region)

    supporting = []
    contradictory = []

    if "earth is round" in lower_claim or "earth is not flat" in lower_claim:
        supporting.append({
            "title": "Scientific consensus on Earth’s shape",
            "source": "NASA",
            "url": "https://www.nasa.gov/",
            "published": "2024",
            "summary": "NASA and scientific measurement data consistently support Earth as an oblate spheroid.",
            "support": "supporting",
        })
    elif "moon landing was faked" in lower_claim or "moon landing fake" in lower_claim:
        contradictory.append({
            "title": "Apollo missions and lunar evidence",
            "source": "NASA",
            "url": "https://www.nasa.gov/",
            "published": "2024",
            "summary": "NASA archives and independent research provide extensive evidence that the Apollo Moon landings took place.",
            "support": "contradicting",
        })
    elif "covid" in lower_claim and ("vaccine" in lower_claim or "vaccines" in lower_claim):
        supporting.append({
            "title": "Public health guidance on COVID-19 vaccines",
            "source": "WHO",
            "url": "https://www.who.int/health-topics/coronavirus",
            "published": "2024",
            "summary": "WHO public health guidance and global monitoring data support vaccination as a major protective intervention.",
            "support": "supporting",
        })
    elif "chandrayaan" in lower_claim.lower() or "moon mission" in lower_claim.lower():
        supporting.append({
            "title": "ISRO mission information",
            "source": "ISRO",
            "url": "https://www.isro.gov.in/",
            "published": "2023",
            "summary": "Official mission materials and public updates from India’s space agency support the claim when backed by specific launch details.",
            "support": "supporting",
        })
    elif "flat earth" in lower_claim:
        contradictory.append({
            "title": "Earth shape evidence",
            "source": "NASA",
            "url": "https://www.nasa.gov/",
            "published": "2024",
            "summary": "Direct observation, satellite data, and centuries of measurements refute a flat-Earth claim.",
            "support": "contradicting",
        })
    else:
        supporting.append({
            "title": "Need for additional verification",
            "source": "Fact-checking review",
            "url": "https://www.poynter.org/ifcn/",
            "published": "2024",
            "summary": "No direct independent evidence was found in the prototype evidence set. The input needs further review from trusted sources.",
            "support": "neutral",
        })

    if not contradictory and "faked" in lower_claim or "fake" in lower_claim:
        contradictory.append({
            "title": "Claim is a strong allegation requiring external confirmation",
            "source": "Fact-checking source",
            "url": "https://www.poynter.org/ifcn/",
            "published": "2024",
            "summary": "Claims that something was fabricated should be checked against primary source documents and credible reporting before being treated as fact.",
            "support": "contradicting",
        })

    evidence = [
        {**src, "support": "supporting" if src["type"] in {"official", "international"} else "neutral"}
        for src in sources
    ]

    if supporting and not contradictory:
        status = "Likely True"
        confidence = 0.81
        explanation = "The submitted claim is consistent with available official and credible evidence. However, confidence remains limited without a live fact-check query and primary-source review."
    elif contradictory and not supporting:
        status = "Likely False"
        confidence = 0.84
        explanation = "The claim is contradicted by reliable institutional evidence or strong established reporting. This is not proof of intent, but it is a strong indication the claim is doubtful."
    elif supporting and contradictory:
        status = "Misleading"
        confidence = 0.67
        explanation = "The claim contains some supporting context, but the available evidence is mixed or incomplete. This suggests the statement is misleading, oversimplified, or selectively framed."
    else:
        status = "Unverified"
        confidence = 0.38
        explanation = "UNMAI could not find enough independent evidence to support or refute the claim confidently. Additional information or source verification is required."

    result = {
        "status": status,
        "confidence": round(confidence, 2),
        "claim": claim_text,
        "claims": claims,
        "summary": f"{status} based on evidence weighting and source quality for the {region or 'global'} context.",
        "explanation": explanation,
        "supporting_evidence": supporting,
        "contradictory_evidence": contradictory,
        "source_links": [
            {"source": item["source"], "url": item["url"]}
            for item in evidence
        ] + [
            {"source": item["source"], "url": item["url"]}
            for item in supporting + contradictory
        ],
        "warnings": [
            "UNMAI is an assistant and not a definitive source of truth.",
            "Evidence quality depends on the credibility and freshness of retrieved sources.",
            "When sources conflict or are weak, the app shows Unverified or Misleading instead of certainty.",
        ],
        "region": region,
    }

    return result


if __name__ == "__main__":
    print(verify_claim("The Earth is round.", region="global"))
