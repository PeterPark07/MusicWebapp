from flask import Flask, render_template, request, send_file
from main import search, download_audio

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_query = request.form.get('search_query')
        urls, titles , durations = search(search_query, 5)
        return render_template('index.html', urls=urls, titles=titles, durations=durations)

    return render_template('index.html')

@app.route('/download', methods=['GET'])
def download():
    url = request.args.get('url')
    response, audio_url , thumbnail = download_audio(url)

    if audio_url:
        return render_template('response.html', audio_url=audio_url, thumbnail=thumbnail)
    else:
        return render_template('response.html', message=response)
   
@app.route('/download_file', methods=['GET'])
def download_file():
    url = request.args.get('url')
    response, audio_url, thumbnail = download_audio(url)

    if audio_url:
        return send_file(audio_url, as_attachment=True)
    else:
        return render_template('response.html', message=response)
    
if __name__ == '__main__':
    app.run()
