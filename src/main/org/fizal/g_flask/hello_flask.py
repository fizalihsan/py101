from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return "Index page {0} {1}".format(request.path, request.method)


@app.route("/hello")
def hello():
    return "Hello World"


@app.route("/hello/<user>")
def hello_user(user):
    return "Hello {0}".format(user)


if __name__ == "__main__":
    app.run()
