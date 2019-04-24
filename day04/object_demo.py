class   Human (object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def xiaozhu(self):
        print('%s %s 小猪'%(self.name,self.age))
    def peiqi(self):
        print('%s  %s  佩奇'% (self.name ,self.age) )

class Tester (Human):
    def word (self):
        print('%s打豆豆'%self.name)
        self.peiqi()
        self.xiaozhu()
if __name__ == '__main__':
        # Human = Human('傻','16')
        # Human.xiaozhu()
        # Human.peiqi()
        Tester = Tester('傻','16')
        tester = Tester
        tester = tester.word()
        print(Tester.name)
