from server import api


@api.route("/")
def root(req, resp):
    resp.text = "root!"
