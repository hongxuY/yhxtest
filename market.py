# -*- encoding:utf-8 -*-

from flask import Flask, jsonify, request
from model.members import db, Member
import config

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://%s:%s@%s:%s/%s" % (
    config.DB_USERNAME, config.DB_PASSWORD, config.DB_HOST, config.DB_PORT, config.DB_NAME)
db.init_app(app)


@app.route('/')
def index():
    return "Hello Flask"


@app.route('/initdb', methods=['POST'])
def init_db():
    db.create_all()
    ret_dic = {
        "return_code": "200",
        "return_msg": "Init db success"
    }
    return jsonify(ret_dic)


# .根据ID获取指定用户
# @app.route('/search',methods = ['GET'])
# def search_member_by_uid():
#     target_uid = request.args['uid']
#     db_ret = Member.query.filter(Member.s_uid == target_uid)
#
#     member_list = []
#     for mem in db_ret:
#         member_info = {"m_uid":mem.m_uid,"s_tel":mem.m_tel,"m_discount":mem.m_disc,"m_score":mem.m_score,"m_active":mem.m_active}
#         member_list.append(member_info)
#
#     ret_dic = {
#         "return_code":"200",
#         "return_msg":"获取用户成功",
#         "count":len(member_list),
#         "student":member_list
#     }
#     return jsonify(ret_dic)


@app.route('/member', methods=['GET','POST',"PATCH","DELETE"])
@app.route('/member/<condition>', methods=['GET', 'PATCH', "PUT", "DELETE"])
def member_actions(condition=None):
    if condition == None and len(request.form)==0:
            if request.method=="GET" and len(request.form)==0:
                returnDict = Member.queryAll()
                return jsonify(returnDict)
            elif request.method!="GET" and len(request.form)==0:
                returnDict={
                "code":400,
                "msg":"请求方式错误，无法获取所有member"
                }
                return jsonify(returnDict)
    elif request.method == "PUT":
        print("[DEBUG] PUT request")
        uid = int(condition.split("_")[-1])
        print("[DEBUG] uid = %s" % uid)
        member = Member.query.filter(Member.uid == uid).first()
        print("[DEBUG] member => %s" % str(member))
        if member==None:
            ret_dic1={
                "return_code": "400",
                "return_msg": "该用户不存在"
            }
            return jsonify(ret_dic1)
        try:
            new_tel = request.form["tel"]
        except:
            new_tel = member.tel
        try:
            new_discount = request.form["discount"]
        except:
            new_discount = member.discount
        try:
            new_score = request.form["score"]
        except:
            new_score = member.score
        try:
            new_active = request.form["active"]
        except:
            new_active = str(member.active)
        ret_dic = Member.update_member_by_uid(uid, member, new_tel, new_discount, new_score, new_active)
        print("[DEBUG] ret_dic = %s" % str(ret_dic))
        return jsonify(ret_dic)

    elif request.method=="GET":

        target_uid = int(condition.split("_")[-1])
        db_ret = Member.query.filter(Member.uid == target_uid)
        member_list = []
        for mem in db_ret:
            member_info = {"uid": mem.uid, "tel": mem.tel, "discount": mem.discount, "score": mem.score,
                           "active": mem.active}
            member_list.append(member_info)

        ret_dic = {
            "return_code": "200",
            "return_msg": "获取用户成功",
            "count": len(member_list),
            "student": member_list
        }
        return jsonify(ret_dic)

    elif request.method == "POST":
        tel = request.form['tel']
        if len(tel) == 11:
            mem_info = Member.add_member(tel)
            ret_dic = {
                "return_code": 200,
                "return_msg": "add member success",
                "member": mem_info
            }
        else:
            ret_dic = {
                "return_code": 400,
                "return_msg": "add member failed, tel not valid",
                "member": {}
            }
        return jsonify(ret_dic)

    elif request.method == "DELETE":
        mem_no = int(condition.split("_")[-1])

        ret_query = Member.query.all()
        for mem in ret_query:
            if mem.uid == mem_no:
                mem.active = 0
                mem.discount = 1

                ret_dic = {"ret_code": "200",
                           "ret_msg": "注销会员成功",
                           "member": {"uid": mem.uid, "tel": mem.tel, "discount": mem.discount, "active": mem.active,
                                      "score": mem.score}
                           }
                return jsonify(ret_dic)

        ret_dic = {"ret_code": "400",
                   "ret_msg": "注销会员失败, uid 不存在"}
        return jsonify(ret_dic)



    elif request.method == "GET":
        if condition.startswith("tel"):
            tel = condition.split("_")[-1]
            ret_dic = Member.search_by_tel(tel)
            ret_dic["return_code"] = 200
            ret_dic["return_msg"] = "get member by tel success"
            return jsonify(ret_dic)



    elif request.method == 'PATCH':
        uid = int(condition.split("_")[-1])
        score = request.form['score']
        db_ret = Member.query.all()
        for member in db_ret:
            if member.uid == uid:
                if score == "":
                    ret_dic = {
                        "return_code": 500,
                        "retuen_msg": "请输入积分值"
                    }
                    return jsonify(ret_dic)
                elif score == "a" or score == "#":
                    ret_dic = {
                        "return_code": 500,
                        "retuen_msg": "请输入正确的积分值"
                    }
                    return jsonify(ret_dic)
                score = int(request.form['score'])
                if score > 0 or score == 0:
                    ret_dic = Member.update_member_score(uid, score)
                    ret_dic["return_code"] = 200
                    ret_dic["return_msg"] = "update score success!"
                    return jsonify(ret_dic)
                else:
                    ret_dic = {
                        "return_code": 500,
                        "retuen_msg": "积分不能为负数，请输入正确的积分值"
                    }
                    return jsonify(ret_dic)
        else:
            ret_dic = {
                "return_code": 400,
                "return_msg": "用户未注册"
            }
        return jsonify(ret_dic)


@app.route('/filter/score')
def filter_member_by_score():
    score = int(request.args['le'])
    ret_dic = Member.filter_member_by_score(score)
    ret_dic["return_code"] = 200
    ret_dic["return_msg"] = "Filter user success"
    return jsonify(ret_dic)


if __name__ == '__main__':
    app.run(host=config.APP_HOST, port=config.APP_PORT)
