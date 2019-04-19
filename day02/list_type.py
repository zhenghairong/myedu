
def list_sel(a):
    print(a[1])
    print(a[-1])
    print(a[0:2])
    print(a[2:])
    print(a[0:])
    print(a[0:4])

if __name__ == '__main__':
    alist = ['你好',1,'你看','你','22']
    list_sel(alist)
