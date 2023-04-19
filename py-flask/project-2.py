from flask import Flask
from flask import redirect, request

app = Flask(__name__)


@app.route("/")
def hello_sprout():
    return "<h1>Hello, NLHS!</h1>"

@app.route("/graduationthreshold")
def lecturer():
    return '<blockquote class="imgur-embed-pub" lang="en" data-id="a/XHyInsD" data-context="false" ><a href="//imgur.com/a/XHyInsD"></a></blockquote><script async src="//s.imgur.com/min/embed.js" charset="utf-8"></script>'

@app.route("/student/<studentName>")
def hello_student(studentName):
    return f"<h1>Hello, {studentName}!</h1>"

@app.route("/ive")
def ive():
    return redirect("https://www.youtube.com/watch?v=6ZUIwj3FgUY")

@app.route("/schoolsong")
def ivevideo():
    return '<iframe width="967" height="544" src="https://www.youtube.com/embed/ypPW7847W0M" title="桃園市內壢高中校歌" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'
if __name__ == "__main__":
    app.run(debug=True)



