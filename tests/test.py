# -*- encoding:utf-8 -*-

import os
import json
import parse


file_path = 'D:/test/'
list = os.listdir(file_path)
for i in list:
    print(i)
    file = 'D:/test/'+i
    with open(file) as file_obj:
        contents = file_obj.read()
        bi = contents.rstrip()
        a= json.loads(bi)
        print (a)
        actObj = a['actObj']
        objType = a['objType']
        traceId = a['traceId']
        actObj = parse.unquote(actObj)
        objType = parse.unquote(objType)
        traceId = parse.unquote(traceId)
        print("traceId:"+traceId+'\n',"actObj:"+actObj+'\n',"objType:"+objType+'\n')
