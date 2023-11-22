from flask import Flask, request, redirect, render_template
from flask import session
import json
app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)

app.secret_key = "123"
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/second_page")
def second_page():
    return  render_template("second_page.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    minnumber = int(request.form["min"])
    maxnumber = int(request.form["max"])
    result = 0
    for i in range(minnumber, maxnumber + 1):
        result += i
    return render_template("calculate.html", result=result)

@app.route("/hello")
def hello():
    name = request.args.get("name", "")
    session["username"] = name
    return f"你好，{name}"

@app.route("/talk")
def talk():
    name = session["username"]
    return f"{name}，我們來聊天吧!"
app.run()


