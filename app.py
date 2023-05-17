from flask import Flask, render_template, request
from main import search, download

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_query = request.form.get('search_query')
        music_result = search(search_query)
        return render_template('index.html', music_result=music_result)

    return render_template('index.html')

# Other routes and functions

if __name__ == '__main__':
    app.run()
