# encoding:utf-8

class wenjuan():
    answer_list =[]
    cont=0
    total=0

    def __init__(self,wechat_id):
        self.name = wechat_id
        wenjuan.cont+=1

    def set_questions(self):
        return 'Q1,Q2,Q3,Q4'
    def answer_questions(self,A1,A2,A3,A4):
        self.answer_list = [A1,A2,A3,A4]
        wenjuan.answer_list.append(self.answer_list)
        self.score = 100
        wenjuan.total+=self.score


    @classmethod
    def get_answer_list_by_id(cls,id):
        answer_list1 = []
        for ans in wenjuan.answer_list:
            answer_list1.append(ans[id-1])
        return answer_list1




wj1 = wenjuan('0x001')
wj1.answer_questions('a','b','c','d')
print (wj1.answer_list)
print (wj1.score)

wj2 = wenjuan('0x002')
wj2.answer_questions('1','2','3','3')
print (wj2.answer_list)
print (wj2.score)

print wenjuan.cont
print wenjuan.total
print wenjuan.get_answer_list_by_id(2)