#encoding:utf-8
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
class Member(db.Model):
    uid=db.Column(db.Integer,primary_key=True,autoincrement=True)
    tel=db.Column(db.String(11),unique=True,nullable=False)
    discount = db.Column(db.FLOAT,nullable=False,default=1)
    score = db.Column(db.Integer,nullable=False,default=0)
    active = db.Column(db.Integer,nullable=False,default=1)

    __tablename__='members'

    @classmethod
    def add_member(cls,tel):
        mem=Member()
        mem.tel=tel
        db.session.add(mem)
        db.session.commit()
        # s搜索显示
        return {'h':'hehe'}
    @classmethod
    def get_members_list_byScore(cls,score):
        members=Member.query.filter(Member.score>=score)
        members_list=[]
        for mem in members:
            members_list.append(mem)
        ret_dic={
            "count":len(members_list),
            "members":members_list
        }
        return ret_dic

    class Member(db.Model):
        uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
        tel = db.Column(db.String(11), unique=True, nullable=False)
        discount = db.Column(db.FLOAT, nullable=False, default=1)
        score = db.Column(db.Integer, nullable=False, default=0)
        active = db.Column(db.Integer, nullable=False, default=1)

        __tablename__ = 'members'

        # 获取积分大于指定值的会员列表
        @classmethod
        def get_member_byScore(cls, score):
            member_list = []
            # 判断传入的le是否为int类型
            # 若score是字母，特殊字符的时候，返回输入正确的值
            # 若score是小数，将score加一在判断。
            try:
                sc = int(score)
                if sc < float(score):
                    sc += 1
            except:
                member_list = ['请输入正确的数值']
                ret_dic = {
                    'members': member_list
                }
                return ret_dic
            # 方法一：从数据库中查找所有用户，
            # 逐个遍历，找到积分大于给定积分的用户，增添进member_list中
            members = Member.query.all()
            for mem in members:
                if mem.score >= sc:
                    member_info = {"uid": mem.uid, 'tel': mem.tel, 'discount': mem.discount, 'score': mem.score,
                                   'active': mem.active}
                    member_list.append(member_info)
            if len(member_list) == 0:
                ret_dic = {
                    "count": 0,
                    "members": member_list
                }
            else:
                ret_dic = {
                    "count": len(member_list),
                    "members": member_list
                }
            return ret_dic
            # 方法二：从数据库中查找到积分大于给定积分的用户，遍历增添进member_list中
            # members = Member.query.filter(Member.score >=int(sc))
            # for mem in members:
            #     member_list.append(mem)
            # ret_dic={
            #  "count":len(member_list),
            #  "members":member_list
            # }
            # return ret_dic



