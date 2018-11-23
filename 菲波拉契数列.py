num=int(input(""))
def fb(n):
    if n==0 or n==1:
        return n
    else:
        return fb(n-1)+fb(n-2)
m=0
Sum=0
while m<=num:
    k=fb(m)
    Sum+=k
    print("{}, ".format(k),end="")
    m+=1
print("{}, {}".format(Sum,int(Sum/m)))
