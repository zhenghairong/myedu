if __name__ == '__main__':
    # w+ 覆盖内容
    # text_io = open('test.text','w+')
    # # write写
    # text_io.write('1111')
    # #  a+追加
    text_io = open('test.text','a+')
    text_io.write('22222')
    # 全部查看
    text_io = open('test.text','r')
    readline = text_io.readline()
    print(readline)