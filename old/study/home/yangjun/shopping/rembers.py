# encoding:utf-8

rembers = [
    {'id':'1','tel':'18812345671','disc':0.95,'credit':0000,'statue':1},
    {'id':'2','tel':'18812345672','disc':0.9,'credit':0000,'statue':1},
    {'id':'3','tel':'18812345673','disc':0.8,'credit':0000,'statue':1}
]

class MemberHelper():

     #定义一个获取会员信息的方法
    @classmethod
    def get_rember_discount(cls,user_tel):

     for rember in rembers:
        if rember['tel']==user_tel:
            return rember['disc']
     return 1.0

    #新增会员


    # @classmethod
    def add_rembers(self,tel):
      for i in rembers:
          if i['tel']==tel:
              print '该手机号已注册'
              return False

      id=len(rembers)+1

      rember = {'id':id,'tel':tel,'disc':0.9,'credit':0000,'statue':1}
      rembers.append(rember)
      print("注册成功")
      print rembers
      return 1


    #获取所有会员列表

    @classmethod
    def rembers_all_list(cls):
        for rem in rembers:
            print("会员编号%s/t,电话%s/t,折扣"%rem['id'],rem['tel'],rem['disc'],rem['credit'])
        return 1

    #根据手机号的后4位获取会员信息
    @classmethod
    def rembers_four(cls,four_last):
        for rem in rembers:
            i=float(rem['tel'])
            a=i%10000
            if four_last==a:
                print("会员编号%s/t,电话%s/t,折扣"%rem['id'],rem['tel'],rem['disc'],rem['credit'])
                return 1


    #根据手机号注销会员（保留）
    @classmethod
    def del_rembers(cls,tel):
        for rem in rembers:
            if str(tel)==rem['tel']:
                print("删除成功")
                return 1


    # 修改会员信息
    @classmethod
    def xiugai_rembers(cls,tel,disc):
        for rem in rembers:
            if str(tel)==rem['tel']:
                disc==rem['disc']
                print(rem)
                return 1


    #会员可累积购物积分
    @classmethod
    def credit_rembers(cls,tel,sum):
        for rem in rembers:
            if str(tel)==rem[tel]:
                print("开始累积积分")
                if rem['credit']<1000:
                    rem['disc']=1
                elif rem['credit']>=1000 and rem['credit']<3000:
                    rem['disc']=0.98
                elif rem['credit']>=3000 and rem['credit']<5000:
                    rem['disc']=0.95
                elif rem['credit']>=5000:
                    rem['disc']=0.9
                print(rem['disc'])
                return rem['disc']
        print("未找到该会员，无法积分")
add=MemberHelper()
tel = raw_input("输入手机号：")
add.add_rembers(tel)
