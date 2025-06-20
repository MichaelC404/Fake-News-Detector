from flask import Flask, render_template, request
from scraper import scrapeArticle  

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def homePage():
    if request.method == "POST":
        url = request.form.get("link")
        try:
            article_text = scrapeArticle(url)
            return render_template("results.html", article=article_text)
        except Exception as e:
            return f"<h2>Error: {e}</h2>"

    return render_template("submitLink.html")
