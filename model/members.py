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
    def search_by_tel(cls,tel):
        member_list=[]
        if len(tel)==11:
            member=Member.query.filter(Member.tel==tel).first()
            member_info={'uid':member.uid,"tel":member.tel,"discount":member.discount,
                         "score":member.score,"active":member .active}
            member_list.append(member_info)
        else:
            db_query=Member.query.filter(Member.tel.endswith(tel))
            for member in db_query:
                member_info={
                    "uid":member.uid,"tel":member.tel,'discount':member.discount,
                    "score":member.score,"active":member.active
                }
                member_list.append(member_info)
        ret_dic={
                    "count":len(member_list),
                    "members":member_list
                }
        return ret_dic
    # def add_member(cls, tel):
    #     mem = Member()
    #     mem.tel = tel
    #     db.session.add(mem)
    #     db.session.commit()
    #     ret_dic = {"active": 1, "discount": 0.95, "score": 100, "tel": tel, "uid": 1}
    #     return ret_dic

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

    @classmethod
    def add_member(cls, tel):
        mem = Member()
        mem.tel = tel
        db.session.add(mem)
        db.session.commit()

        ret_dic = cls.search_by_tel(tel)['members'][0]
        return ret_dic

    @classmethod
    def update_member_by_uid(cls, uid,member ,new_tel, new_discount, new_score, new_active):
        print("[DEBUG] update_member_by_uid-> ")
        if uid=="" or new_tel=="" or new_discount=="" or new_score=="" or new_active=="":
            ret_dic={"return_code": "400",
            "return_msg": "修改的属性不能为空"}
            return ret_dic
        elif new_active !="0" and new_active !="1":
            ret_dic = {"return_code": "400",
                       "return_msg": "激活状态只能为0或1"}
            return ret_dic
        elif int(new_score)<0:
            ret_dic = {"return_code": "400",
                       "return_msg": "积分不能为负数"}
            return ret_dic
        print("[DEBUG] update_member_by_uid-> target member info {%s, %s, %s, %s, %s}" % (member.uid, member.tel, member.discount, member.score, member.active))
        print("[DEBUG] update_member_by_uid-> target member change value {%s, %s, %s, %s, %s}" % (member.uid, new_tel, float(new_discount), int(new_score), int(new_active)))
        member.tel = new_tel
        member.active = int(new_active)
        member.discount = float(new_discount)
        member.score = int(new_score)
        print("[DEBUG] update_member_by_uid-> target member after info {%s, %s, %s, %s, %s}" % (member.uid, member.tel, member.discount, member.score, member.active))

        db.session.commit()

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
    def get_members_by_id(cls, uid):
        member_list = []
        member = Member.query.filter(Member.uid == uid).first()
        for mem in member:
            if mem['uid'] == uid:
                member_list.append(mem)
                break
        ret_dic={
            "count":len(member_list),
            "member":member_list
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
            "code":200,
            "msg": "queryAll success",
            "count": len(memberList),
            "student": memberList
        }
        return returnDict







