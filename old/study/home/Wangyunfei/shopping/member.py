# coding:utf-8
from Wangyunfei.shopping.test.test_homework.shopping import memberHelp
from SALING import saling

def Saling():
    user_tel = raw_input('请输入你的手机号：')
    user_discount = memberHelp.get_member_discount(user_tel)
    product_list=[]
    while True:
       pro_info=saling.get_product_input()
       if pro_info == "Q":
           break
       else:
            product_list.append(pro_info)
            print ('商品已添加')



    pay_list,pay_total = saling.caularment_payment(product_list,user_discount)


    output = saling.format_out_msg(pay_list,pay_total)
    print (output)
if __name__=='__main__':
    Saling()









