a = int( input("請輸入 a 的值：") )
b = int( input("請輸入 b 的值：") )
c = int( input("請輸入 c 的值：") )

if a>b and a>c:
    print("最大值為 " + str(a) )
else :
    if b>c:
        print("最大值為 " + str(b) )
    else:
        print("最大值為 " + str(c) )