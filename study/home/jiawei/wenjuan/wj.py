#encoding:utf-8
class wenjuan():
    counter=0
    total_score=0

    def __init__(self,wechat_id):
        self.name=wechat_id
        wenjuan.counter+=1

    def set_questions(self):
        return "Q1,Q2,Q3,Q4,Q5"

    def answer_questions(self,a1,a2,a3,a4,a5):
        self.answer_list=[a1,a2,a3,a4,a5]
        self.score=100
        wenjuan.total_score+=self.score

    @classmethod
    def get_answer_list_by_id(cls,id):
        target_answer_list=[]
        for ans in wenjuan.total_answer_list:
            target_answer_list.append(ans[id-1])
        return target_answer_list

wj1=wenjuan('qt0001')
wj1.answer_questions('A','B','D','B','C')
print(wj1.answer_list)
print(wj1.score)

wj2=wenjuan('qt0002')
wj2.answer_questions('C','B','D','A','C')
print(wj2.answer_list)
print(wj2.score)

print(wenjuan.counter)
print(wenjuan.total_score)
print(wenjuan.get_answer_list_by_id(3))