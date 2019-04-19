
def astr_demo():
    astr = '5'
    print(astr)
    print(type(astr))

def float_damo():
    afloat = 0.1
    print(afloat)
    print(type(afloat))
def abb_damo(a,b):
    print(a+b)
def type_zh():
    aint = 1
    print(aint)
    print(type(str(aint)))
    print(type(int(aint)))
    print(type(str(aint)))
def str_join():
    a='你好'
    b="你好"
    c=521
    d=521
    print(a+b+str(c)+str(d))
    print('a是%s b是%s c是%s d是%s'%(a,b,c,d))
    print('%s %s %s %s'%(a,b,c,d))
def jianfa_demo(a,b):
    c = a-b
    return c
if __name__ == '__main__':
    # int_demo()
    #  str_demo()
    # float_damo()
    # abb_damo(5,8,9)
    # abb_damo('你','好','吗')
    # abb_damo('你好','521','121')
    # type_zh()
    # str_join
    jianfa_demo(9,6)
    print(jianfa_demo(9,6))






