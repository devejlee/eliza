from flask import Flask, render_template, request
import random
from main import start_chat, chat

app = Flask(__name__)

chat_log = []

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        posted = chat(request.form["user"])
        chat_log.append('User: ' + request.form["user"])
        chat_log.append(posted)
        return render_template("index.html", chat_log=chat_log)
    else:
        return render_template("index.html", start_chat="ELIZA: " + random.choice(start_chat))


if __name__ == "__main__":
    app.run(debug=True)
