#encoding:utf-8
from Members import MembersHelp
from client import Saling
def Sale():

  user_tel = raw_input('**********欢迎使用XXshopping系统************\n请输入你的手机号码:\n')
  user_discount = MembersHelp.get_member_discount(user_tel)


  product_list=[]

  while True:
     pro_info=Saling.get_product_input()
     if pro_info == "Q":
         break
     else:
         product_list.append(pro_info)

  pay_list,pay_total = Saling.caularment_payment(product_list,user_discount)

  print (pay_list)

  output = Saling.format_out_msg(pay_list,pay_total)
  print (output)



if __name__ =='__main__':
   Sale()