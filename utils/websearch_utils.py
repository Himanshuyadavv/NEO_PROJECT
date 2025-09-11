import requests
from config.config import SERPAPI_KEY

def live_web_search(query):
    """Perform live web search using SerpAPI."""
    if not SERPAPI_KEY:
        return ["[⚠️ No SERPAPI_KEY found in config]"]
    url = f"https://serpapi.com/search.json?q={query}&api_key={SERPAPI_KEY}"
    response = requests.get(url).json()
    results = response.get("organic_results", [])
    return [r["snippet"] for r in results[:3]] if results else ["No results found."]
