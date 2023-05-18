from flask import Flask, render_template, request, send_file
from main import search, download_audio

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_query = request.form.get('search_query')
        music_result, youtube_url = search(search_query)
        download_url = f'/download?url={youtube_url}'
        return render_template('index.html', music_result=music_result, youtube_url=youtube_url, download_url=download_url)

    return render_template('index.html')

@app.route('/download', methods=['GET'])
def download():
    url = request.args.get('url')
    response, audio_url , name = download_audio(url)

    if audio_url and name:
        filename = name  # Specify the desired filename here
        return send_file(audio_url, as_attachment=True, attachment_filename=filename)
    elif audio_url:
        return send_file(audio_url, as_attachment=True)
    else:
        return render_template('response.html', message=response)

if __name__ == '__main__':
    app.run()
