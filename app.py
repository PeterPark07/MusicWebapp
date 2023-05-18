from flask import Flask, render_template, request, redirect
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

    # Replace this with your logic to download the audio file using the URL
    # For example, you can use the `download()` function from the `main` module
    response, download_url = download_audio(url)

    if download_url:
        return redirect(download_url)
    else:
        return render_template('response.html', message=response)

# Other routes and functions

if __name__ == '__main__':
    app.run()
