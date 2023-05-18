import yt_dlp as youtube_dl
from youtubesearchpython import VideosSearch
import os

ytdl_opts = {'format': 'bestaudio/best',
             'postprocessors': [{'key': 'FFmpegExtractAudio',
                                 'preferredcodec': 'best',
                                 'preferredquality': 'best'}]}

def search(query):
  search = VideosSearch(query, limit=1)
  results = search.result().get('result')
  if not results:
      return "No videos found for that query." , None
  
  selected_video = results[0]
  url = f"https://www.youtube.com/watch?v={selected_video['id']}"
  return f"{selected_video['title']}..." , url

def download_audio(url):
  try:
    with youtube_dl.YoutubeDL() as ydl:
        info = ydl.extract_info(url, download=False)
        formats = info['formats']
        audio_formats = [f for f in formats if f.get('vcodec') == 'none']
        audio_formats = audio_formats[-2]
        download_url = audio_formats.get('url')
        return None , url
  except:
    return 'Could not download file' , None
  
def delete(path):
  os.remove(path)
