def isPrime(num):
    for i in range(2,num):
        if num%i==0:
            return False
          
    return True
while True:
    try:
        num=eval(input("请输入一个整数："))
    except:
        print("输入错误！请输入一个整数：")
        continue
    if type(num) is not int:
        print("请输入一个整数：")
        continue
    if num == -1:
        break
    if isPrime(num):
        print("{} 是质数.".format(num))
    else:
        print("{}不是质数.".format(num))
