# coding:UTF-8

class wenjuan():
    count=0
    total_score=0
    def __init__(self,wechat_id):
        self.name=wechat_id

    def set_questions(self):
        return "Q1,Q2,Q3,Q4"

    def anwser_question(self,a1,a2,a3,a4):
        self.anwser_list=[a1,a2,a3,a4]
        self.score = 100
        wenjuan.count +=1

     @classmethod
    def get_answer_list_by_id(cls,id):
         taget_answer_list=[]
        for ans in wenjuan.total_answer_list:
            target_answer_list.append(ans[id-1])
        return tar_answer_list


wj1 = wenjuan("0x001")
wj1.anwser_question("A",'B','C','D')
print (wj1.anwser_list)
print(wj1.score)

wj2= wenjuan("0x002")
wj2.anwser_question('A','B','B','C')
print(wj2.anwser_list)
print(wj2.score)
print wenjuan.count