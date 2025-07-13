
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    url = data.get("url", "")
    return jsonify({
        "meta_description": "مثال لوصف SEO",
        "arabic_keywords": "عطور، فخامة، نفحات شرقية",
        "english_keywords": "perfume, elegant, oriental notes",
        "arabic_seo_title": "عنوان SEO لعطر فخم",
        "english_seo_title": "Luxury Perfume SEO Title",
        "image_url": ""
    })

if __name__ == "__main__":
    app.run(debug=True)
