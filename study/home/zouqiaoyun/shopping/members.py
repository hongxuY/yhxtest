# coding:utf-8
members=[
    {"id":"1","tel":"18902371234","discount":0.80},
    {"id":"2","tel":"18302531239","discount":0.90},
    {"id":"3","tel":"13503321236","discount":0.95},
    {"id":"4","tel":"12590178902","discount":0.98}
]

class membersHelper():

    @classmethod
    def get_member_discount(cls,u_tel):
        for member in members:
            if member["tel"]==u_tel:
               return member["discount"]
        return 1.0














