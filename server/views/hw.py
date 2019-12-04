from server import api


@api.route("/hello")
def hello(req, resp):
    resp.text = "hello world!"


@api.route("/")
def hello(req, resp):
    resp.text = "root!"
