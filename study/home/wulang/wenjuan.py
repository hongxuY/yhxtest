# enconding:utf-8


class wenjuan():
    count = 0
    total_score = 0
    def __init__(self, wechat_id):
        self.name = wechat_id
        wenjuan.count += 1
    def set_questions(self):
        return"Q1,Q2,Q3,Q4"
    def answer_questions(self,a1,a2,a3,a4):
        self.answer_list = [a1,a2,a3,a4]
        self.score = 100
        wenjuan.total_score +=self.score
    @classmethod
    def get_answer_list_by_id(cls,id):
        target_answer_list = []
        for ans in wenjuan.total_answer_list:
            target_answer_list.append(ans[id-1])
            return target_answer_list




wj1 = wenjuan('0x001')
wj1.answer_questions('A','B','C','D')
print(wj1.answer_list)
print(wj1.score)

wj2 = wenjuan('0x002')
wj2.answer_questions('D','C','B','A')
print(wj2.answer_list)
print(wj2.score)

print(wenjuan.count)
print(wenjuan.get_answer_list_by_id(1))
print (wenjuan.get_answer_list_by_id(4))



class WenJuan():

    counter = 0

    def __init__(self):
        print("WenJuan 被初始化了，counter+1")
        WenJuan.counter += 1

    def get_questions(cls):
        print("Q1\nQ2\nQ3")

    @classmethod
    def get_wj_counter(cls):
        return cls.counter


wj1 = WenJuan()
print(wj1.get_questions())

wj2 = WenJuan()
print(wj2.get_questions())

wj3 = WenJuan()
print(wj3.get_questions())

print(WenJuan.get_wj_counter())
