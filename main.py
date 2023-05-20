import yt_dlp as youtube_dl
from youtubesearchpython import VideosSearch

def search(query, n):
    search = VideosSearch(query, limit=n)  # Search with a limit of n results
    results = search.result().get('result')
    if not results:
        return None, None ,None

    urls = []
    titles = []
    durations =[]
    for video in results:
        if video['duration']: 
            urls.append(video['link'])
            titles.append(video['title'])
            durations.append(video['accessibility']['duration'] )

    return urls, titles , durations 

def download_audio(url):
  try:
    with youtube_dl.YoutubeDL() as ydl:
        info = ydl.extract_info(url, download=False)
        thumbnail = [i['url'] for i in info['thumbnails'] if i['url'].endswith('.jpg')][-1] 
        download_url = [f.get('url') for f in info['formats'] if f.get('vcodec') == 'none'][-2]
        return None , download_url , thumbnail
  except:
    return 'Could not download file', None , None
