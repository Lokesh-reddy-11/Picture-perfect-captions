from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import os
from main import generate_caption  # Import the captioning function

app = Flask(__name__)
UPLOAD_FOLDER = 'images/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "image" not in request.files:
        return redirect(request.url)

    file = request.files["image"]

    if file.filename == "":
        return redirect(request.url)

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Generate caption using the uploaded image
        caption = generate_caption(filepath)
        return render_template("index.html", caption=caption, image_url=f"/{filepath}")

if __name__ == "__main__":
    app.run(debug=True,port='5001')
