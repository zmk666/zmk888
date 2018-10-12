money=input("请输入带有符号的金额:")
if money[-1]in['￥']:
    Z=eval(money[0:-1])/6
    print("转换后的钱是{:.2f}$".format(Z))
elif money[-1]in['$']:
    M=6*eval(money[0:-1])
    print("转换后的钱是{:.2f}￥".format(M))
else:
    print("输入格式错误")
