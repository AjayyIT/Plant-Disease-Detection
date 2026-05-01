from flask import Flask, render_template, request
import os
from predict import predict_image

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    result, confidence, treatment = predict_image(filepath)

    return render_template(
        "index.html",
        result=result,
        confidence=round(confidence * 100, 2),
        treatment=treatment,
        image_path=filepath
    )

if __name__ == "__main__":
    app.run(debug=True)