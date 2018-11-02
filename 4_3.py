m,n=eval(input("请输入整数，中间用逗号隔开:"))
x,y=m,n
r =x%y
while r >0:
    x,y=y,r
    r=x%y
print("{}和{}是最大公约数是：{}；最小公倍数是：{:.0f}".format(m,n,y,m*n/y))
