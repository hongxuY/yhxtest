# coding:utf-8

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Member(db.Model):
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tel = db.Column(db.String(11), unique=True,nullable=False)
    discount = db.Column(db.FLOAT,nullable=False,default=1)
    active= db.Column(db.Integer,nullable=False, default=1)
    score=db.Column(db.Integer,nullable=False, default=0)

    __tablename__ = "members"


    @classmethod
    def add_member(cls,tel):
        mem=Member()
        mem.tel=tel
        db.session.add(mem)
        db.session.commit()



    # @classmethod
    # def