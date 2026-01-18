import os
import json
import re
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

CLAIM_PROMPT = """
Extract factual claims from the text.
Return ONLY valid JSON array like:

[
  { "claim": "text", "category": "finance | ai | aerospace | economy" }
]

Text:
{document_text}
"""

def extract_claims_with_regex(text):
    """
    Fallback extractor using simple heuristics
    """
    claims = []

    patterns = [
        r"Bitcoin.*?\$[0-9,]+",
        r"GPT-\d+.*?(delayed|released|paused)",
        r"Starship.*?(failure|launched|crashed)",
        r"GDP.*?[-]?\d+\.?\d*%",
        r"Unemployment.*?\d+\.?\d*%"
    ]

    for p in patterns:
        matches = re.findall(p, text, re.IGNORECASE)
        for m in matches:
            claims.append({
                "claim": m,
                "category": "economy"
            })

    return claims


def extract_claims(text):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": CLAIM_PROMPT.format(document_text=text)}],
            temperature=0
        )

        raw = response.choices[0].message.content.strip()
        parsed = json.loads(raw)

        if isinstance(parsed, dict):
            parsed = [parsed]

        valid = [c for c in parsed if isinstance(c, dict) and "claim" in c]

        if valid:
            return valid

        raise ValueError("No valid claims from GPT")

    except Exception:
        # FALLBACK MODE
        return extract_claims_with_regex(text)
