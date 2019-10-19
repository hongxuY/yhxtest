# coding:utf-8

class Salesclient():

    @classmethod
    def get_product_input(cls):
        while True:
            try:
                user_input = raw_input("请输入商品的价格或是Q进行结算：")
                return float(user_input)

            except ValueError:
                if user_input == "Q":
                    return "Q"
                print("用户输入错误，请重新输入")

    @classmethod
    def calcultor_payment(cls,product_list,discount):
        total = 0
        pay_list = []
        for i in range(len(product_list)):
            payment_item = [i + 1, product_list[i], product_list[i] * discount]
            pay_list.append(payment_item)
            total += product_list[i] * discount
        return pay_list, total

    @classmethod
    def format_out_msg(cls,list, total):
        out_msg = "商品\t原价\t折后价\n"
        for prod in list:
            out_msg += "%s\t%s\t%s\n" % (prod[0], prod[1], prod[2])
        out_msg += "-----------------------\n"
        out_msg += "总价：\t%s" % total
        return out_msg