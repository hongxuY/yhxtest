# -*- coding:utf-8 -*- 
#Author: LQF

import os
import json
from urllib import parse


file_path = 'D:/5.7.4ios'
list = os.listdir(file_path)
for i in list:
    print(i)
    file = 'D:/5.7.4ios/'+i
    with open(file, encoding='utf-8') as file_obj:
        contents = file_obj.read()
        bi = contents.rstrip()
        a= json.loads(bi)
        actObj = a['actObj']
        objType = a['objType']
        traceId = a['traceId']
        actObj = parse.unquote(actObj)
        objType = parse.unquote(objType)
        traceId = parse.unquote(traceId)
        print("traceId:"+traceId+'\n',"actObj:"+actObj+'\n',"objType:"+objType+'\n')
