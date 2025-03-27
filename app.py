from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Dictionary API endpoint
API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"

@app.route("/", methods=["GET", "POST"])
def index():
    word_data = None  # To store the dictionary data

    if request.method == "POST":
        word = request.form.get("word")  # Get the word from the form
        if word:
            response = requests.get(API_URL + word)
            
            if response.status_code == 200:
                word_data = response.json()[0]  # Extract the first result
            else:
                word_data = {"error": "Word not found"}

    return render_template("index.html", word_data=word_data)

if __name__ == "__main__":
    app.run(debug=True)
