Fuhao=input("请输入温度符号:")
if Fuhao in['F','f']:
    t=eval(input("请输入温度值:"))
    C=(t-32)/1.8
    print("转换后的温度是{:.2f}C".format(C))
elif Fuhao in['C','c']:
    t=eval(input("请输入温度值:"))
    F=1.8*t+32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")
