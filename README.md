# TikTokDownloader-dlpanda-scraper

Simple TikTok Image and Video Downloader in a Few Lines of Code using dlpanda.com

## Overview

This Python script allows you to download images and videos from TikTok using the `dlpanda.com` service. It leverages the `requests` library for HTTP requests and `BeautifulSoup` for parsing HTML.

## Features

- **Download TikTok Images and Videos:** Easily fetch media content from TikTok using a provided URL.
- **Simple Interface:** Use a straightforward class with a few methods to handle the download process.
- **Error Handling:** Includes basic error handling for network issues.

## Installation

1. Clone the repository:

```git clone https://github.com/Mectron2/TikTokDownloader-dlpanda-scraper.git```

2. **Navigate to the project directory:**

```cd TikTokDownloader-dlpanda-scraper```

3. **Install the required packages:**

```pip install -r requirements.txt```

## Usage

```
from TikTokDownloader import TikTokDownloader
downloader = TikTokDownloader()
URL = "YOUR_TIKTOK_URL_HERE"
content, content_type = downloader.download_content(URL)
if content_type == 'image':
    for img_url in content:
        print(f"Image URL: {img_url}")
elif content_type == 'video':
    print(f"Video URL: {content}")
elif content_type == 'error':
    print("Failed to retrieve content.")
```

## Configuration
### Token: 
Default token is G7eRpMaa. You might need to obtain your own token if there are authentication issues or if the service requires it. The easiest way to get a token is to go to ```https://dlpanda.com/```, paste the link to any video from TikTok.
After a short wait, you'll be redirected to a similar URL:
```https://dlpanda.com/?url=https%3A%2F%2Fwww.tiktok.com%2F%40androee.ae%2Fvideo%2F7413017745178053893&token=G7eRpMaa```
As you can see, there is a token `G7eRpMaa` at the end of the URL. It's currently the default, but if it's changed, you can pass it to the class constructor like this:
```downloader = TikTokDownloader(token = "YOUR_TOKEN_GOES_HERE")```
### Headers:
By default dlpanda does not require request headers, but if you encounter access issues, try adding headers to the class constructor like this:
```downloader = TikTokDownloader(headers = {"YOUR_HEADERS": "GOES_HERE", "HEADER1": "HEADER1"})```
And of course, these 2 approaches can be combined like this:
```downloader = TikTokDownloader(token = "YOUR_TOKEN_GOES_HERE", headers = {"YOUR_HEADERS": "GOES_HERE", "HEADER1": "HEADER1"})```
