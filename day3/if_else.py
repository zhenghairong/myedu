# 不等大于前面的值走else大于走if
def if_damo():
    a = 1 > 2
    if a:
        print('对')
    else:
        print('错')
# 上下级关系要搞清楚 结束时候是else,
def ifel_demo():
    a = 2
    if a == 0:
        print('a是0')
    elif a == 1:
        print('a是1')
    elif a == 2:
        print('a是2')
    elif a == 3:
        print('a是3')
    else:
      print('a是%s'%a)
    print('if结束')

if __name__ == '__main__':
    ifel_demo()
