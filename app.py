from flask import Flask, render_template, request
from main import search, download

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_query = request.form.get('search_query')
        music_result ,url = search(search_query)
        return render_template('index.html', music_result=music_result)

    return render_template('index.html')

@app.route('/download', methods=['GET'])
def download():
    # Retrieve the track ID from the query parameters
    track_id = request.args.get('track_id')

    # Implement the download logic based on the track ID
    # Replace the code below with your actual download logic
    # For example, you can use the `youtube_dl` library to download the audio file
    # and return it as a response to the user
    return f"Download endpoint for track ID: {track_id}"

# Other routes and functions

if __name__ == '__main__':
    app.run()
