import re

def extract_claims(text):
    claims = []

    patterns = [
        r"Bitcoin.*?\$[0-9,]+",
        r"Unemployment.*?\d+\.?\d*%",
        r"GDP.*?-?\d+\.?\d*%",
        r"GPT-\d+.*?(released|delayed|paused)",
        r"Starship.*?(launched|failed|crashed)"
    ]

    for pattern in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        for match in matches:
            claims.append({
                "claim": match
            })

    # Fallback: if nothing matched, extract numeric sentences
    if not claims:
        sentences = re.split(r"[.\n]", text)
        for s in sentences:
            if any(char.isdigit() for char in s):
                claims.append({"claim": s.strip()})

    return claims
