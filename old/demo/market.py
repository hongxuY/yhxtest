# -*- encoding:utf-8 -*-

from flask import Flask, jsonify, request
from old.demo import db, Member
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


@app.route('/member', methods=['GET', 'POST', "PATCH", "DELETE"])
@app.route('/member/<condition>', methods=['GET', 'PATCH', "PUT", "DELETE"])
def member_actions(condition=None):
    if condition == None and len(request.form) == 0:
        if request.method == "GET" and len(request.args) == 0:
            returnDict = Member.queryAll()
            return jsonify(returnDict)
        elif request.method != "GET" and len(request.args) == 0:
            returnDict = {
                "code": 400,
                "msg": "请求方式错误，无法获取所有member"
            }
            return jsonify(returnDict)
    if condition == None and len(request.form) == 0:
        if request.method == "GET" and len(request.form) == 0:
            returnDict = Member.queryAll()
            return jsonify(returnDict)
        elif request.method != "GET" and len(request.form) == 0:
            returnDict = {
                "code": 400,
                "msg": "请求方式错误，无法获取所有member"
            }
            return jsonify(returnDict)
    elif request.method == "PUT":
        uid = int(condition.split("_")[-1])
        member = Member.query.filter(Member.uid == uid).first()
        if member == None:
            ret_dic1 = {
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
        return jsonify(ret_dic)




    elif request.method == "GET":
        if condition.startswith("uid_"):
            try:
                target_uid = int(condition.split("_")[-1])
            except:
                ret_dic = {
                    "return_code": "400",
                    "return_msg": "uid输入错误"
                }
                return jsonify(ret_dic)
            db_ret = Member.query.filter(Member.uid == target_uid)

            member_list = []
            for mem in db_ret:
                member_info = {"uid": mem.uid, "tel": mem.tel, "discount": mem.discount, "score": mem.score,
                               "active": mem.active}
                member_list.append(member_info)
            if len(member_list) == 0:
                ret_dic = {
                    "return_code": "400",
                    "return_msg": "uid不存在"
                }
                return jsonify(ret_dic)
            else:
                ret_dic = {
                    "return_code": "200",
                    "return_msg": "获取用户成功",
                    "count": len(member_list),
                    "members": member_list
                }
                return jsonify(ret_dic)

        elif condition.startswith("tel_"):
            tel = condition.split("_")[-1]
            ret_dic = Member.search_by_tel(tel)
            return jsonify(ret_dic)

        # 添加新用户到数据库，根据手机号码
    elif request.method == 'POST':
        tel = request.form['tel']
        member1 = Member.query.filter(Member.tel == tel).first()
        if member1 != None:
            ret_dic = {
                "return_code": "400",
                "return_msg": "该电话号码用户已注册"
            }
            return jsonify(ret_dic)

        # tel str字符 判断长度，是否11位来确定有没有必要往下进行
        if len(tel) == 11:
            # 用isdigit()函数来判断是否为数字，是数字返回True 否则返回false
            result = request.form['tel'].isdigit()
            if result == True:
                # 是数字
                mem_info = Member.add_member_by_tel(tel)
                ret_dic = {
                    "return_code": 200, "return_msg": "add member success",
                    "member": mem_info
                }
                return jsonify(ret_dic)
            else:
                # 不是数字
                ret_dic = {
                    "return_code": 508, "return_msg": "add member failed, exists",
                }
                return jsonify(ret_dic)
        else:
            # 不是11位
            ret_dic = {
                "return_code": 508, "return_msg": "add member failed, exists",
            }
            return jsonify(ret_dic)

    # 根据用户ID注销会员
    elif request.method == "DELETE":
        try:
            mem_no = int(condition.split("_")[-1])
        except:
            ret_dic = {"ret_code": "400",
                       "ret_msg": "请输入数字！"}
            return jsonify(ret_dic)
        ret_query = Member.query.all()
        for mem in ret_query:
            if mem.uid == mem_no:
                if mem.active == 0:
                    ret_dic = {"ret_code": "400",
                               "ret_msg": "会员已注销，请重新输入！"}

                    return jsonify(ret_dic)

                mem.active = 0
                mem.discount = 1
                db.session.commit()

                ret_dic = {"ret_code": "200",
                           "ret_msg": "注销会员成功！",
                           "member": {"uid": mem.uid, "tel": mem.tel, "discount": mem.discount, "active": mem.active,
                                      "score": mem.score}
                           }
                return jsonify(ret_dic)

        ret_dic = {"ret_code": "400",
                   "ret_msg": "注销会员失败, uid 不存在"}
        return jsonify(ret_dic)



    elif request.method == 'PATCH':
        uid = int(condition.split("_")[-1])
        db_ret = Member.query.filter(Member.uid == uid).first()
        if db_ret == None:
            ret_dic = {
                "return_code": 400,
                "return_msg": "用户未注册"
            }
            return jsonify(ret_dic)
        try:
            if db_ret.uid == uid:
                score = int(request.form['score'])
                if isinstance(score, int):
                    if score > 0 or score == 0:
                        ret_dic = Member.update_member_score(uid, score)
                        ret_dic["return_code"] = 200
                        ret_dic["return_msg"] = "update score success!"
                        return jsonify(ret_dic)
                    else:
                        ret_dic = {
                            "return_code": 500,
                            "return_msg": "积分不能为负数，请输入正确的积分值"
                        }
                        return jsonify(ret_dic)
        except:
            ret_dic = {
                "return_code": 500,
                "return_msg": "请输入正确积分值"
            }
            return jsonify(ret_dic)


@app.route('/filter/score')
def filter_member_by_score():
    try:
        score = int(request.args['le'])
    except:
        ret_dic = {
            "return_code": 500,
            "return_msg": "积分输入错误，请输入正确的积分"
        }
        return jsonify(ret_dic)
    if score < 0:
        ret_dic = {
            "return_code": 500,
            "return_msg": "积分不能为负数"
        }
        return jsonify(ret_dic)
    ret_dic = Member.filter_member_by_score(score)
    ret_dic["return_code"] = 200
    ret_dic["return_msg"] = "Filter user success"
    return jsonify(ret_dic)


if __name__ == '__main__':
    app.run(host=config.APP_HOST, port=config.APP_PORT)
