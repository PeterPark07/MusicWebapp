import yt_dlp as youtube_dl
from youtubesearchpython import VideosSearch

def search(query , n):
    search = VideosSearch(query, limit=n)  # Search with a limit of 5 results
    results = search.result().get('result')
    if not results:
        return "No videos found for that query.", None

    music_results = []
    for video in results:
        url = f"https://www.youtube.com/watch?v={video['id']}"
        music_results.append((video['title'], url))

    return music_results
  
def download_audio(url):
  try:
    with youtube_dl.YoutubeDL() as ydl:
        info = ydl.extract_info(url, download=False)
        formats = info['formats']
        audio_formats = [f for f in formats if f.get('vcodec') == 'none']
        download_url = audio_formats[-2].get('url')
        extension = audio_formats[-2].get('ext')
        video_title = info.get('title')
        video_title_with_extension = f"{video_title}.{extension}"
        return None , download_url , video_title_with_extension 
  except:
    return 'Could not download file', None, None
