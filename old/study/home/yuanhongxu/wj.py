#coding:utf-8

class wenjuan():
    counter=0
    total_secore=0
    total_anstower_list=[]

    def __init__(self,wechat):
        self.name=wechat
        wenjuan.counter+=1

    def set_question(self,):
        return ("q1,q2,q3,q4")

    def answer_question(self,a1,a2,a3,a4):
        self.list=[a1,a2,a3,a4]
        self.secore=100
        wenjuan.total_secore+=self.secore
        wenjuan.total_anstower_list.append(self.list)


    @classmethod
    def get_answer_list_by_id(self,id):
        trage_list=[]
        for i in wenjuan.total_anstower_list:
            trage_list.append(i[id-1])
        return trage_list


wj1=wenjuan("aaa")
wj1.answer_question("a","b","c,","d")
print (wj1.list)
print (wj1.secore)

print (wenjuan.counter)
print (wenjuan.total_secore)

wj2=wenjuan("bbb")
wj2.answer_question("d","c","b,","d")
print (wj2.list)
print (wj2.secore)

print (wenjuan.counter)
print (wenjuan.total_secore)
print (wenjuan.get_answer_list_by_id(3))

