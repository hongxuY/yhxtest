# coding:utf-8
class saling():
    @classmethod
    def get_product_input(cls):
        while True:
            try:
                pro_info = raw_input('请输入你的商品或者Q:\n')
                return float(pro_info)
            except ValueError:
                if pro_info == "Q":
                    return "Q"
                print ('输入有误，请重新输入')

    @classmethod
    def caularment_payment(cls,product_list,user_discount):
        payment_list=[]
        total=0
        for i in range(len(product_list)):
            payment_item=[i+1,product_list[i],product_list[i]*user_discount]
            payment_list.append(payment_item)
            total+=product_list[i] * user_discount
        return payment_list,total

    @classmethod
    def format_out_msg(cls,list,total):
        out_msg = "商品\t原价\t折后价\n"
        for i in list:
            out_msg += "%s\t%s\t%s\n"%(i[0],i[1],i[2])
        out_msg += "-----------\n"
        out_msg += "总价：\t%s"%total
        return out_msg