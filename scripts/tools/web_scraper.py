import requests
import urllib.parse
from bs4 import BeautifulSoup

class WebScout:
    def search_intel(self, query, timeframe='w'):
        """Scrapes Google News using robust URL encoding."""
        print(f"--- [Scouting Live Web Intelligence for: {query}] ---")
        
        base_url = "https://google.com"
        params = {
            "q": query,
            "tbm": "nws",
            "tbs": f"qdr:{timeframe}"
        }
        url = f"{base_url}?{urllib.parse.urlencode(params)}"
        
        # FIX: Ensure this line has exactly 8 spaces (or 2 tabs) and matches the 'url' line
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            headlines = [h.text for h in soup.find_all('h3')[:3]]
            return headlines if headlines else ["The field is quiet. No news detected."]
        except Exception as e:
            return [f"Connection lost: {e}"]
