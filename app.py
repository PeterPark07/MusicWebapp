from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the search query from the form
        search_query = request.form.get('search_query')

        # Process the search query and retrieve a single music result from the API
        # Replace the code below with your actual API integration logic
        music_result = None

        return render_template('index.html', music_result=music_result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
