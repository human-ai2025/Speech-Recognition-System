from flask import Flask, request, jsonify, render_template
import random
from prediction import Keyword_Spotting_Service
import os

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')


@app.route("/predict", methods=["POST"])
def predict():
    """Endpoint to predict keyword
        :return (json): This endpoint returns a json file with the following format:
            {
                "keyword": "down"
            }
    """
    # get audio file and save it
    audio_file = request.files["file"]
    file_name = str(random.randint(0, 100000))
    audio_file.save(file_name)

    # instantiate keyword spotting service singleton and get prediction
    kss = Keyword_Spotting_Service()
    predicted_keyword, ind = kss.predict(file_name)

    # we don't need the audio file any more - let's delete it!
    os.remove(file_name)

    # send back result as a json file
    result = {"keyword": predicted_keyword}
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=False)
