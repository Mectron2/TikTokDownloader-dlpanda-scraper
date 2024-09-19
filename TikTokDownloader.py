import requests
import urllib.parse
from bs4 import BeautifulSoup

class TikTokDownloader:
    def __init__(self, token='G7eRpMaa'):
        self.token = token
        self.headers = {
            # Your headers here
        }
    
    def encode_url(self, url: str) -> str:
        """Encode URL for safe HTTP request"""
        return urllib.parse.quote(url, safe='')

    def download_content(self, url: str):
        """Main function to download content from TikTok"""
        try:
            link = f'https://www.dlpanda.com/?url={self.encode_url(url)}&token={self.token}'
            response = requests.get(link, headers=self.headers, timeout=(10, 30))
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')

            if soup.find('source') is None:
                return self._extract_images(soup), 'image'
            else:
                return self._extract_video(soup), 'video'

        except requests.RequestException as e:
            print(f"An error occurred while fetching the content: {e}")
            return None, 'error'

    def _extract_images(self, soup):
        """Extract image URLs from HTML content"""
        images = []
        for el in soup.find_all('img'):
            src = el.get('src')
            if src and ("photomode" in src or 'snapcdn.app' in src):
                images.append(src)
        return images

    def _extract_video(self, soup):
        """Extract video URL from HTML content"""
        src = soup.find('source').get('src')
        if src and src.startswith('//'):
            src = 'https:' + src
        return src