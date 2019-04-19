import json
adict = {"username":"yansl","password":"123456"}
bdict = {'5':"yansl","password":[2,5]}

cdict_str = '{"username":"yansl","password":"123456"}'
def dict_sel():
    print(adict["username"])
    print(bdict['5'])
def dict_del():
    b = adict.pop('password')
    print(b)
def dict_update():
    adict['username'] = '郑'
    print(adict)

def dict_add():
    adict.update(bdict)
    print(adict)

    cdict = dict(adict,**bdict)
    print(cdict)
def dict_add1():
    adict['rrr'] = '女'
    print(adict)


def dict2str():
    print(type(adict))
    adict_str = json.dumps(adict)
    print(adict_str)
    print(type(adict_str))

def dict1str():
    print(type(adict))
    cdict_str = json.dumps(adict)
    print(cdict_str)
    print(type(cdict_str))
#     字典类型转字符串
def str2dict():
    print(type(cdict_str))
    cdict = json. loads(cdict_str)
    print(cdict_str)
    print(type(cdict_str))



if __name__ == '__main__':
    # str2dict()
    # dict2str()
    # dict_add1()
    # dict_sel()
    # dict_del()
    # dict_add()
    # dict_update()
