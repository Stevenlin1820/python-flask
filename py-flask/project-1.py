from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_NLHS():
    return "<h1>Hello, NLHS! My name is Steven</h1>"


if __name__ == "__main__":
    app.run()
