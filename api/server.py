import json

from flask import Flask, request, render_template_string
from OCR.read_recepit import get_text_from_image
from recommendation.recommendation import find_recommended_things
app = Flask(__name__)


@app.route('/')
def index():
    return '''Server Works!'''


@app.route('/ocr', methods=['POST'])
def process():
    if request.method == "POST":
        image = request.files['image']
        name, ammount, date = get_text_from_image(image)
        x = {
            "name": name,
            "ammount": ammount,
            "date": date
        }
        return render_template_string(json.dumps(x))
    return "KRIVO"


@app.route('/recommend', methods=['POST'])
def recommend():
    if request.method == "POST":
        data = request.get_json()
        recommended_things = find_recommended_things(data["item"])
        x = {
            "recommendations": recommended_things,
        }
        return render_template_string(json.dumps(x))
    return "KRIVO"

if __name__ == '__main__':
    app.run(debug=True)
