import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def verify_claim(claim):
    search_results = tavily.search(query=claim, max_results=5)

    output = "🔍 **Live Web Verification (Search-based)**\n\n"
    output += f"**Claim:** {claim}\n\n"
    output += "**Evidence from web sources:**\n"

    for r in search_results.get("results", []):
        title = r.get("title", "Source")
        url = r.get("url", "")
        output += f"- {title} ({url})\n"

    output += (
        "\n**Status:** Requires review / Likely inaccurate if sources contradict the claim.\n"
        "_Note: Automated LLM verification unavailable due to API restrictions._"
    )

    return output
