# coding:utf-8

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Member(db.Model):
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tel = db.Column(db.String(11), unique=True, nullable=False)
    discount = db.Column(db.FLOAT, nullable=False, default=1)
    score = db.Column(db.Integer, nullable=False, default=0)
    active = db.Column(db.Integer, nullable=False, default=1)

    __tablename__ = "members"

    @classmethod
    def search_by_tel(cls, tel):
        try:
            tel = int(tel)
        except:
            ret_dic = {
                "msg": "请输入正确的电话号码！",
                "ret_code": "400",
            }
            return ret_dic

        tel = str(tel)
        if len(tel) == 11:
            dbquery = Member.query.all()
            for member in dbquery:
                if member.tel == tel:
                    member_info = {'uid': member.uid, "tel": member.tel, "discount": member.discount,
                                   "score": member.score, "active": member.active}
                    ret_dic = {
                        "msg": "search member by tell success",
                        "ret_code": "200",
                        "member": member_info
                    }
                    return ret_dic
                else:
                    ret_dic = {
                        "msg": "该号码还不是会员！",
                        "ret_code": "400",
                    }
            return ret_dic
        elif len(tel) == 4:
            dbquery = Member.query.all()
            member_list = []

            for member in dbquery:
                if member.tel.endswith(tel) == True:
                    member_info = {
                        "uid": member.uid, "tel": member.tel, 'discount': member.discount,
                        "score": member.score, "active": member.active
                    }
                    member_list.append(member_info)
                    ret_dic = {
                        "msg": "search member by tell success",
                        "ret_code": "200",
                        "member": member_list
                    }
            if len(member_list) == 0:
                ret_dic = {
                    "msg": "search member by tell false",
                    "ret_code": "400",
                    "member": member_list
                }
            return ret_dic
        else:
            ret_dic = {
                "msg": "请输入正确的电话号码！",
                "ret_code": "400",
            }
            return ret_dic

    @classmethod
    def update_member_score(cls, uid, score):
        member = Member.query.filter(Member.uid == uid).first()
        score_before = member.score
        member.score = score_before + score
        db.session.commit()
        ret_dic = {"uid": member.uid, 'tel': member.tel, 'score_before': score_before,
                   'score_after': member.score,
                   'score_change': score}
        return ret_dic

    @classmethod  # 添加会员
    def add_member_by_tel(cls, tel):
        member = Member()
        member.tel = tel
        db.session.add(member)
        db.session.commit()
        ret_dic = cls.search_by_tell(tel)['members'][0]
        return ret_dic

    @classmethod
    def update_member_by_uid(cls, uid, member, new_tel, new_discount, new_score, new_active):
        if uid == "" or new_tel == "" or new_discount == "" or new_score == "" or new_active == "":
            ret_dic = {"return_code": "400",
                       "return_msg": "修改的属性不能为空"}
            return ret_dic
        elif new_active != "0" and new_active != "1":
            ret_dic = {"return_code": "400",
                       "return_msg": "激活状态只能为0或1"}
            return ret_dic
        elif int(new_score) < 0:
            ret_dic = {"return_code": "400",
                       "return_msg": "积分不能为负数"}
            return ret_dic
        elif len(new_tel) != 11:
            ret_dic = {"return_code": "400",
                       "return_msg": "电话号码为11位"}
            return ret_dic
        elif float(new_discount) > 1 or float(new_discount) < 0:
            ret_dic = {"return_code": "400",
                       "return_msg": "折扣为0到1之间"}
            return ret_dic

        try:
            new_tel = int(new_tel)
        except:
            ret_dic = {"return_code": "400",
                       "return_msg": "电话号码为数字"}
            return ret_dic

        member.tel = str(new_tel)
        member.active = int(new_active)
        member.discount = float(new_discount)
        member.score = int(new_score)
        try:
            db.session.commit()
        except:
            ret_dic = {"return_code": "400",
                       "return_msg": "手机号是唯一的，您输入的手机号与数据库冲突"}
            return ret_dic
        ret_dic = {"uid": member.uid, 'tel': member.tel, 'discount': member.discount,
                   'score': member.score, 'active': member.active}
        return ret_dic

    @classmethod
    def inactive_member(cls, uid):
        for i in range(len(Member.members)):
            if Member.members[i]['uid'] == uid:
                Member.members[i]['active'] = '0'

            ret_dic = {
                'uid': Member.members[i]['uid'],
                'tel': Member.members[i]['tel'],
                'active': '0',
                'discount': '1'
            }
            return ret_dic

    @classmethod
    def get_members_by_uid(cls, uid):
        member_list = []
        member = Member.query.filter(Member.uid == uid).first()
        for mem in member:
            if mem['uid'] == uid:
                member_list.append(mem)
                break
        ret_dic = {
            "count": len(member_list),
            "member": member_list
        }

        return ret_dic

    @classmethod
    def queryAll(cls):
        memberList = []
        dbmember = Member.query.all()
        for member in dbmember:
            newMember = {"uid": member.uid, "tel": member.tel, "discount": member.discount,
                         "score": member.score, "active": member.active}
            memberList.append(newMember)
        returnDict = {
            "code": 200,
            "msg": "queryAll success",
            "count": len(memberList),
            "member": memberList
        }
        return returnDict

        # 根据手机号查找会员列表

    @classmethod
    def search_by_tell(cls, tel):
        member_list = []
        if len(tel) == 11:
            member = Member.query.filter(Member.tel.endswith(tel)).first()
            member_info = {'uid': member.uid, 'tel': member.tel, 'discount': member.discount, 'score': member.score,
                           'active': member.active}
            member_list.append(member_info)
        else:
            db_query = Member.query.filter(Member.tel.endswith(tel))
            for member in db_query:
                member_info = {'uid': member.uid, 'tel': member.tel, 'discount': member.discount, 'score': member.score,
                               'active': member.active}
                member_list.append(member_info)
        ret_dic = {
            'count': len(member_list),
            'members': member_list
        }
        return ret_dic

    @classmethod
    def filter_member_by_score(cls, score):
        members = Member.query.all()
        member_list = []
        for member in members:
            if member.score >= score:
                newMember = {"uid": member.uid, "tel": member.tel, "discount": member.discount,
                             "score": member.score, "active": member.active}
                member_list.append(newMember)
        ret_dic = {
            "member": member_list
        }
        return ret_dic
