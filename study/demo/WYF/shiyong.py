# encoding:utf-8
from flask import Flask, jsonify, request
from WYF.shiyong_mem import db,Member

app = Flask(__name__)
# 配置数据库连接
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@127.0.0.1:3306/supermarket"
db.init_app(app)


@app.route('/')
def index():
    return 'Hellow Flask'


@app.route('/initdb', methods=['POST'])
def init_db():
    db.create_all()
    ret_dic = {
        'return_code': 200,
        'return_msg': 'Init db success'
    }
    return jsonify(ret_dic)


# 根据手机号添加会员  ---童一鉴
@app.route('/member', methods=['POST'])
def member_actions(condition=None):
    # 1.处理创建
    if request.method == 'GET':
        if condition == None:
            member_list = Member.get_all_members()
            member_list['return_code'] = 200
            member_list['return_msg'] = '获取用户成功'
    elif request.method == 'POST':
        tel = request.form['tel']
        mem_info = Member.add_member_by_tel(tel)
        ret_dic = {
            "return_code": 200, "return_msg": "add member success",
            "member": mem_info
        }
        return jsonify(ret_dic)


# 根据手机号码查找会员列表  ---liu
@app.route('/member/<condition>' , methods=['GET'])
def get_members_by_tel(condition=None):
    if request.method == 'GET':
        if condition.startswith('tel_'):
            tel = condition.split('_')[-1]
            ret_dic = Member.search_by_tel(tel)
            ret_dic['return_code'] = 200
            ret_dic['return_msg'] = 'Get Member by tel success'
            return jsonify(ret_dic)
        else:
            uid = int(condition.split('_')[-1])
            ret_dic = Member.serch_member_by_uid(uid)
            if len(ret_dic) == 0:
                ret_dic['return_code'] = 400
                ret_dic['return_msg'] = 'Get Member by uid faild'
            else:
                ret_dic['return_code'] = 200
                ret_dic['return_msg'] = 'Get Member by uid success'
            return jsonify(ret_dic)

# 查找大于给定积分的用户--闫振兴
@app.route('/filter/score')
def get_members_byScore():
    score = request.args['le']
    ret_dict = Member.get_member_byScore(score)
    ret_dict['return_code'] = 200
    ret_dict['return_msg'] = "Filter user success"
    print (ret_dict)
    return jsonify(ret_dict)



#根据用户金额更改用户积分  杨俊
@app.route('/member/<condition>' , methods=['PATCH'])
def surpermark_member(condition=None):
    if condition != None:
        if request.method == 'PATCH':
            uid = int(condition.split("_")[-1])
            score = int(request.form['score'])
            ret_dic = Member.update_member_score(uid, score)
            ret_dic['return_code'] = 200
            ret_dic['return_msg'] = 'update score success'
            return jsonify(ret_dic)


@app.route('/member', methods=['PUT'])
def update_members_info():
    mem_tel=request.form['tel']
    mem_discount=request.form['discount']
    mem_score=request.form['score']
    mem_active=request.form['active']

    target_members=Member.query.filter(Member.uid == uid)[0]
    target_members.tel=mem_tel
    target_members.discount=mem_discount
    target_members.score=mem_score
    target_members.active = mem_active
    db.session.commit()

    ret_dic = {
        'return_code': '200',
        'return_msg': 'Update members success',
        'tel': mem_tel,
        'discount': mem_discount,
        'score':mem_score,
        'active': mem_active
    }
    return jsonify(ret_dic)


# 根据UID注销
@app.route('/member/<condition>', methods=['DELETE'])
def delete_member(condition=None):
    if  request.method == "DELETE":
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
                           "ret_msg": "注销会员成功",
                           "member": {"uid": mem.uid, "tel": mem.tel, "discount": mem.discount, "active": mem.active,
                                      "score": mem.score}
                           }
                return jsonify(ret_dic)
        else:
            ret_dic = {"ret_code": "400",
                           "ret_msg": "注销会员失败, uid 不存在"}
            return jsonify(ret_dic)








if __name__ == '__main__':
    app.run( port=5000, debug=True)
