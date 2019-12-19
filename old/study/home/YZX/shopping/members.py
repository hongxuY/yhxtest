#encoding:utf-8
members=[
    {'id':1,'tel':'13312345671','disc':0.98},
    {'id':2,'tel':'13312345672','disc':0.95},
    {'id':3,'tel':'13312345673','disc':0.9},
    {'id':4,'tel':'13312345674','disc':0.8}
]
class MembersHelp():
    @classmethod
    def get_member_discount(cls,tel):
        for member in members:
            if member['tel']==tel:
                return member['disc']
        return 1.0
    def add_member(self,tel):
        self.tel = tel
        disc=0.9
        for i in members:
            if i[tel]==self.tel:
                print ("手机号码已经注册。")
                return False
        id=len(members)
        str(self.tel)
        member = {"id":id,"tel":tel,"disc":disc}
        members.append(members)
        return members
