# coding:utf-8


from flask import Flask, request,jsonify

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.get_data()
        password = request.get_data()
        print("username:%s"%(username))
        print("password:%s"%(password))
        if username=="yuan"and password==123:
            resp={
                "return_code":200,
                "return_msg":"登录成功"
            }
        else:
            resp = {
                "return_code": 500,
                "return_msg": "登录失败"
            }

        return jsonify(resp)



if __name__ == '__main__':
    app.run()
