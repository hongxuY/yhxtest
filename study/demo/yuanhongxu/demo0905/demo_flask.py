# coding:utf-8
from flask import Flask, request

app = Flask(__name__)


@app.route("/mm", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
def login():
    if request.method == "GET":
        user = request.form["user"]
        pwd = request.form["pwd"]
        return ("GET%s,%s" % (user, pwd))
    elif request.method == "POST":
        user=request.form["user"]
        pwd=request.form["pwd"]
        return ("POST%s,%s"%(user,pwd))
    elif request.method == "PUT":
        return ("PUT")
    elif request.method == "PATCH":
        return ("PATCH")
    elif request.method == "DELETE":
        return ("DELETE")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5678")
