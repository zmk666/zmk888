k = 5
x = eval(input("请输入0~9之间的整数:"))
b = 0
while x != k:
    b += 1
    if(x > k):
        print("遗憾，太大了")
    else:
        print("遗憾，太小了")
    x = eval(input("请输入0~9之间的整数:"))
print("预测{}次，你猜中了".format(b))

