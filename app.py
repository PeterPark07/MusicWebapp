from flask import Flask, render_template, request
from main import search, download

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_query = request.form.get('search_query')
        music_result ,url = search(search_query)
        print(music_result , url)
        return render_template('index.html', music_result=music_result , url = url)

    return render_template('index.html')

@app.route('/download', methods=['GET'])
def download():
    track_id = request.args.get('track_id')

    # Replace this with your logic to download the audio file using the track_id
    # For example, you can use youtube-dl to download the audio
    # Make sure to provide the correct path to the downloaded file
    file_path = 'path/to/downloaded/file.mp3'

    return send_file(file_path, as_attachment=True)

# Other routes and functions

if __name__ == '__main__':
    app.run()
