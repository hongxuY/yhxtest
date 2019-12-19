# encoding:utf-8
class salesclient():
    @classmethod
    def get_product_input(cls):
        while True:
            try:
                user_input = raw_input("请输入商品价格，或输入Q进行结算")
                return float(user_input)
            except ValueError:
                if user_input == "Q":
                    return "Q"
                print ("输入有误，请重新输入")
    @classmethod
    def payment(cls,goods_list,user_disc):
        payment_list=[]
        total = 0
        for i in range(len(goods_list)):
            payment1= [i+1,goods_list[i],goods_list[i]*user_disc]
            payment_list.append(payment1)
            total += goods_list[i]*user_disc
        return payment_list,total
    @classmethod
    def format_out_msg(cls,list,total):
        out_msg = "商品ID\t原价\t折后价\n"
        for prod in list:
            out_msg += "%s\t%s\t%s\n" % (prod[0], prod[1], prod[2])
        out_msg+= "--------------------\n"
        out_msg+= "总价=\t%s" %total
        return out_msg