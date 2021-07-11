from flask import Flask, render_template, request
import random
from main import start_chat, test

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])

def home():
    if request.method == "POST":
        posted = test(request.form["user"])
        return render_template("index.html", start_chat="ELIZA: " + random.choice(start_chat), posted=posted)
    else:
        return render_template("index.html", start_chat="ELIZA: " + random.choice(start_chat))


if __name__ == "__main__":
    app.run(debug=True)
