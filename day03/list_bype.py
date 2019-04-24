

def list_update():
    alist = ['你','好','吗',1,'不','好','我',888]

    alist.insert(0,888)
    print(alist)

def list_zj():
    alist = [1,2,3,4,5,6]
    alist.pop(0)

    print(alist)
if __name__ == '__main__':
    # list_update()
    list_zj()