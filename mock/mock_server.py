# coding:utf-8
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # resp = {
        #     "msg": "获取成功",
        #     "code": 200,
        #     "data":{
        #         "status":3
        #     },
        #     "tid": "63e85ad7-c913-403e-b775-526364e97960"
        # }

        resp = {
            "msg": "获取成功",
            "code": 200,
            "data": [{
                "orderId": 1157118,
                "totalPremium": "0",
                "insEndDate": "2020-11-27 00:00:00",
                "policyNo": "1019112764893428476983011920",
                "type": 5,
                "productName": "药神保.抗癌保险（升级版）",
                "productCode": "PH19",
                "wesureToken": "577b484452d34bb193e2b1e8266ac9c3",
                "insuredName": "陈剑锋",
                "insBeginDate": "2019-11-28 00:00:00",
                "remark": "被保人",
                "status": 1
            }, {
                "orderId": 1157117,
                "totalPremium": "0",
                "insEndDate": "2020-11-27 00:00:00",
                "policyNo": "1019112763683239455983012417",
                "type": 5,
                "productName": "药神保.抗癌保险",
                "productCode": "PH24",
                "insuredName": "陈剑锋",
                "insBeginDate": "2019-11-28 00:00:00",
                "remark": "被保人",
                "status": 1
            }],
            "tid": "d668c8b2-2ded-4260-a3b4-728f891207dc"
        }
        return jsonify(resp)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5001")
