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
    response,  thumbnail = show_audio(url)

    if thumbnail:
        return render_template('response.html', audio_url=url, thumbnail=thumbnail)
    else:
        return render_template('response.html', message=response)
   
@app.route('/download_file', methods=['GET'])
def download_file():
    url = request.args.get('url')
    response, filepath = download_audio(url)

    if filepath:
        return send_file(filepath, as_attachment=True)
    else:
        return render_template('response.html', message=response)
    
if __name__ == '__main__':
    app.run()
