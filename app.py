from flask import Flask, render_template, request
from pyfingerprint.pyfingerprint import PyFingerprint
import cv2
import numpy as np
import os
import webbrowser
app = Flask(__name__)

fingerprint_folder = "fingerprint"

def load_images(folder):
    images = []
    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        if img is not None:
            images.append((filename, img))
    return images

def match_fingerprint(test_image, fingerprint_images):
    method = cv2.TM_CCOEFF_NORMED
    results = []

    for filename, fingerprint_image in fingerprint_images:
        # Resize fingerprint_image to match the size of test_image
        resized_fingerprint_image = cv2.resize(fingerprint_image, (test_image.shape[1], test_image.shape[0]))

        result = cv2.matchTemplate(test_image, resized_fingerprint_image, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        results.append((filename, max_val))

    results.sort(key=lambda x: x[1], reverse=True)
    return results

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Handle the uploaded image and perform fingerprint matching
        uploaded_file = request.files["file"]
        if uploaded_file:
            test_image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_GRAYSCALE)
            fingerprint_images = load_images(fingerprint_folder)
            results = match_fingerprint(test_image, fingerprint_images)
            return render_template("result.html", results=results)

    return render_template("index.html")

if __name__ == "__main__":
    webbrowser.open('http://127.0.0.1:5000/')
    app.run(debug=True)
