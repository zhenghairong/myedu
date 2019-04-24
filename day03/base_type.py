# 键值对=字典类型
#  import json  调用 json才可以转
adict = {"username":"yansl","password":"123456"}
bdict = {'5':"yansl","password":[2,5]}
import json

# 转换字符串类型
cdict_str = '{"username":"yansl","password":"123456"}'

#def 是关键字  关键字后面是方法名
def lianxi_demo():
    print('111')

#  减法类型 加 return返回值
def jianfa_demo(a,b):
    b = 9-2
    return b

#  add 加法类型
def add_bpe(c,b):
    b = 9+2
    print(b)

# int整数类型
def  int_demo():
    aint = 6
    print(aint)
    print(type(aint))

# str 字符串类型
def str_demo():
    astr = '你好'
    print(astr )
    print(type(astr))

#flout 小数类型
def flout_type():
    aflout = 0.2
    print(aflout)
    print(type(aflout))

# pop 是删除方法  删除类型
def del_type():
    adel = ['你好','你','1','饿哦',1]
    adel.pop()
    print(adel)

# append 增加末尾方法 增加类型
def list_zj():
    alist = [ '你','好','hao',1]
    alist.append('1')
    print(alist)

# join连接
def str_join():
    a = 3
    b = 2
    c = '你'
    print(a,b,str(c))

# 转换类型
def zhuanghuan_type():
    astr = '3'
    print(astr)
    print(type(astr))
    # astr类型转换int类型  要转回来则反向
    print(type(int(astr)))

# 前后切片调换
def list_type():
    alist = ['你好','我','1',2,3]
    c = alist[:2]
    b = alist[2:]
    b.append(c)
    print(b)

#  json.dumps 调用方法 字典转字符串
def dict1str():
    print(type(adict))
    adict_str =json.dumps(adict)
    print(type(adict_str))

# json.loada 调用方法 字符串转字典
def str2dict():
    print(type(cdict_str))
    adict = json.loads(cdict_str)
    print(type(adict))
#



if __name__ == '__main__':
    str2dict()
    dict1str()
    # list_type()
    # str_join()
    # zhuanghuan_type()
    # list_zj()
    # del_type()
   # str_demo()
   #  flout_type()
     # int_demo()
    # lianxi_demo()
    # jianfa_demo()
    # print(jianfa_demo())
    # add_bpe()
    # print(add_bpe())

