from flask import Flask, render_template, request
import os
from soil_analysis.analyze import analyze_soil
from soil_analysis.crop_recommend import recommend_crop

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create upload folder if not exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    if "image" not in request.files:
        return "No file uploaded"

    file = request.files["image"]

    if file.filename == "":
        return "No selected file"

    # Save image
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    # Analyze soil
    soil_type = analyze_soil(filepath)

    # Recommend crops
    crops = recommend_crop(soil_type)

    return render_template(
        "index.html",
        soil_type=soil_type,
        crops=crops,
        image_path=filepath
    )


if __name__ == "__main__":
    app.run(debug=True)