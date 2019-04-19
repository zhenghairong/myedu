
def list_sel(a):
    print(a[1])
    print(a[-1])
    print(a[0:2])
    print(a[2:])
    print(a[0:])
    print(a[0:4])

def list_del():
    alist = ['你好',4,'好的','自己','学习']
    alist.pop()
    print(alist)
    alist.pop(2)
    print(alist)
    alist.pop(1)
    print(alist)
    alist.pop(-1)
    print(alist)

def list_add():
    alist = [4,5,6,7,'你好','嗯','1']
    alist .append('嗯嗯嗯嗯嗯')
    print(alist)
    blist  = [1,2,3,4]
    alist.append(blist)
    print(alist)
def list_update():
    alist = ['你好',4,'好的','自己','学习',[1,2,3,4]]
    alist[0] = 3
    print(alist)
if __name__ == '__main__':
    # alist = ['你好',1,'你看','你','22']
   # list_sel(alist)
   # list_del()
   #  list_add()
   list_update()