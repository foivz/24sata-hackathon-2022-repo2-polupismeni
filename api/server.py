import json

from flask import Flask, request, render_template_string
from OCR.read_recepit import get_text_from_image
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


if __name__ == '__main__':
    app.run(debug=True)
