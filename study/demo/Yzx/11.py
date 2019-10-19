# 查找大于给定积分的用户
@app.route('/filter/score')
def get_members_byScore():
    score = request.args['le']
    ret_dict = Member.get_member_byScore(score)
    ret_dict['return_code'] = 200
    ret_dict['return_msg'] = "Filter user success"
    print (ret_dict)
    return jsonify(ret_dict)


    # 获取积分大于指定值的会员列表
    @classmethod
    def get_member_byScore(cls,score):
            member_list=[]
            # 判断传入的le是否为int类型
            # 若score是字母，特殊字符的时候，返回输入正确的值
            # 若score是小数，将score加一在判断。
            try :
                sc=int(score)
                if sc<float(score):
                    sc+=1
            except :
                member_list=['请输入正确的数值']
                ret_dic={
                    'members':member_list
                }
                return ret_dic
            # 方法一：从数据库中查找所有用户，
            # 逐个遍历，找到积分大于给定积分的用户，增添进member_list中
            members=Member.query.all()
            for mem in members:
                if mem.score>=sc:
                    member_info = {"uid": mem.uid,'tel':mem.tel,'discount':mem.discount,'score':mem.score,'active':mem.active}
                    member_list.append(member_info)
            if len(member_list)==0:
                ret_dic= {
                "count": 0,
                "members": member_list
                }
            else:
                ret_dic = {
                "count": len(member_list),
                "members": member_list
                }
            return ret_dic
            # 方法二：从数据库中查找到积分大于给定积分的用户，遍历增添进member_list中
            # members = Member.query.filter(Member.score >=int(sc))
            # for mem in members:
            #     member_list.append(mem)
            # ret_dic={
            #  "count":len(member_list),
            #  "members":member_list
            # }
            # return ret_dic