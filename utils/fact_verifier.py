import os
from openai import OpenAI, RateLimitError
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def verify_claim(claim):
    # Always do live web search
    search_results = tavily.search(query=claim, max_results=5)

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f"""
You are a fact checker.

Claim:
"{claim}"

Based on the web data below, say whether the claim is Verified, Inaccurate, or False.
Explain briefly and mention sources.

Web data:
{search_results}
"""
            }],
            temperature=0
        )

        return response.choices[0].message.content

    except RateLimitError:
        #  GRACEFUL FALLBACK
        summary = "⚠️ OpenAI quota exhausted. Showing live web evidence instead.\n\n"
        summary += "🔎 Web search results:\n"

        for r in search_results.get("results", []):
            summary += f"- {r.get('title')} ({r.get('url')})\n"

        summary += "\nBased on the above sources, this claim requires manual review."
        return summary
