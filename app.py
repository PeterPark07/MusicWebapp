from flask import Flask, render_template, request
from main import search, download

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_query = request.form.get('search_query')
        music_result ,url = search(search_query)
        print(music_result , url)
        download_url = f'/download?url={url}'
        return render_template('index.html', music_result=music_result , youtube_url = url , download_url = download_url)

    return render_template('index.html')

@app.route('/download', methods=['GET'])
def download():
    url = request.args.get('url')

    # Replace this with your logic to download the audio file using the track_id
    # For example, you can use the `download()` function from the `main` module
    file_path = download(url)

    return send_file(file_path, as_attachment=True)

# Other routes and functions

if __name__ == '__main__':
    app.run()
