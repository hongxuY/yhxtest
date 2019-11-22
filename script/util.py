# -*- encoding: utf-8 -*-

import json
import hashlib


def signMD5(dict):
    AppSecret = "6d5ee6f5-cb6b-4510-86e9-3d415c17a500"
    # AppSecret = "ab4176ca-11de-4c58-bda6-10892c61f42a"
    # od_str = json.dumps(dict, sort_keys=True, ensure_ascii=False)
    od_str = json.dumps(dict, separators=(',', ':'), sort_keys=True, ensure_ascii=False)
    # od_str = json.dumps(OrderedDict(dict))
    od_str = od_str.encode("utf-8")
    m = hashlib.md5()
    m.update(od_str+AppSecret)
    sign_str = m.hexdigest()
    return sign_str


def updateRequest(dict):
    sign = signMD5(dict)
    dict['sign'] = sign
    return dict



