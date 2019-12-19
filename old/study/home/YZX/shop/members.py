#encoding:utf-8
members=[
    {'id':'1','tel':'18845871680','disc':0.9},
    {'id':'2','tel':'18845095099','disc':0.1}
]
class Members():
    @classmethod
    def get_disc_by_tell(cls,tel):
        for member in members:
            if tel == member['tel']:
                print member['disc']
                return member['disc']
        return 1.0



