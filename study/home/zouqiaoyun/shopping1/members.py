
# coding:utf-8


members=[
    {"id":"1","tel":"18902371234","discount":0.80,"status":"active","jifen":0},
    {"id":"2","tel":"18302531239","discount":0.90,"status":"active","jifen":0},
    {"id":"3","tel":"13503321236","discount":0.95,"status":"active","jifen":0},
    {"id":"4","tel":"12590178902","discount":0.98,"status":"active","jifen":0}
]



class membersHelper1():

#获得会员的折扣
     @classmethod
     def get_member_discount(cls,tel):
            for i in members:
                if i["tel"]==tel:
                    return i["discount"]
            return 1.0



#增加会员
     @classmethod
     def add_newmember(cls,tel):

             for i in members:
                     if i['tel'] == tel:
                         print ("已经注册过会员")
                         return 1.0

             id = len(members) + 1
             newmember = {"id": id, "tel": tel, "discount": 0.9, "status": "active", "jifen": 0}
             members.append(newmember)
             print ('注册成功')
             print(newmember)
             return newmember



#获取会员列表信息
     @classmethod
     def get_allmembers(cls):
        members_format = "会员id\t会员电话\t\t\t会员折扣\t\t状态\t\t积分\n"
        for i in members:
           members_format+="%s\t\t%s\t\t%s\t\t%s\t\t%s\n"%(i["id"],i["tel"],i["discount"],i["status"],i["jifen"])
        print(members_format)
        return 1.0

#根据手机号后四位获取会员信息
     @classmethod
     def get_member_list_by_lastfournumber(cls,lastfourtelnumber):
            text_list=[]
            a=list(lastfourtelnumber)
            for i in members:
                b=list(i["tel"])
                if b[7:11]==a:
                        text_list.append(i)
                        print("匹配到的会员信息:%s"%text_list)

            return text_list

#根据手机号注销会员
     @classmethod
     def zhuxiao_member(cls,tel):
         for i in members:
                 if i["tel"] == tel:
                     i["status"]="inactive"
                     print("注销的会员：%s"%i)
         return i

#修改会员信息（手机号和折扣）
     @classmethod
     def update_member(cls,tel,status,update_choice,new_tel,new_discount):
         for i in members:
             if i["tel"]==tel and  i["status"]=="inactive":
                 print("该用户已经被注销了")
                 return 1.0
             elif i["tel"]==tel and i["status"]=="active":

              if update_choice=="1":
                i["tel"]=new_tel
                print("修改后的会员信息%s"%i)
                return i
              elif update_choice=="2":
                    i["discount"]=new_discount
                    print("修改后的会员信息%s"%i)
                    return i
              else :
                  i["tel"]=new_tel
                  i["discount"] =new_discount
                  print("修改后的会员信息%s"%i)
                  return i





#会员可积累购物积分（1元=1积分，1000积分可以打98折，3000积分打95折，5000积分打九折）
     @classmethod
     def accumulated_shopping_points(cls,tel,total):
         for i in members:
             if i["tel"] == tel and i["status"] == "active":
                 print ("找到会员，开始累计积分。")
                 i['jifen'] += total
                 print("总积分：%s"%i["jifen"])
                 if i['jifen'] < 1000 and i["jifen"]>0:
                    i['discount'] = i["discount"]
                    print("最后的折扣：%s" % (i["discount"]))
                 elif i['jifen'] >= 1000 and i['jifen'] < 3000:
                      i['discount'] = i["discount"]*0.98
                      print("最后的折扣：%s" % (i["discount"]))
                 elif i['jifen'] >= 3000 and i['jifen'] < 5000:
                      i['discount'] = i["discount"] * 0.95
                      print("最后的折扣：%s" % (i["discount"]))
                 elif i['jifen'] >= 5000:
                      i['discount'] = i["discount"] * 0.9
                      print("最后的折扣：%s" % (i["discount"]))
                 else:
                     i['discount']=1
                     print("最后的折扣：%s"%(i["discount"]))

                 return i["jifen"],i["discount"]




