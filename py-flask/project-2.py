from flask import Flask
from flask import redirect, request

app = Flask(__name__)
password = "bingchilling"


@app.route("/")
def hello_sprout():
    return "<h1>Hello, Sprout!</h1>"


@app.route("/price")
def fee():
    return "<p>兩個階段都1700</p>"


@app.route("/student/<studentName>")
def hello_student(studentName):
    return f"<h1>Hello, {studentName}!</h1>"


@app.route("/secret")
def getSecret():
    try:
        inputPassword = request.args.get("password")
        if password != inputPassword:
            raise Exception("Password incorrect")
        return "<h1>我的房子還蠻大的</h1>"
    except Exception as e:
        return f"403 Forbidden : {e}", 403


@app.route("/ive")
def ive():
    return redirect("https://www.youtube.com/watch?v=6ZUIwj3FgUY")


if __name__ == "__main__":
    app.run(debug=True)
