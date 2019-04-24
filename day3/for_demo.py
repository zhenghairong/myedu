
alist = ('小','猪','佩','奇',1,2)
   #  for 关键字 i是循环次数 in是关键字 range 迭代器函数 最后打印 i 循环次数 打印值
def for_demo1():
    for i in range(8):
        print(i)
        print(111)
#  两个从第一个数开始数 到第二个前一位
def for_demo():
    for i in range(11,5,-2):
        print(i)
#  遍历 循环alist里面的所有值
def for_list():
    for i in alist:
        print(i)
#第二种遍历    获取 list长度    通过长度设置循环 打印i
def for_list1():
    a = len(alist)
    for i in range(a):
        print(alist[i])
if __name__ == '__main__':
    # for_demo()
   # for_list()
   for_list1()
