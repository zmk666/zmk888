import random
a=['羊1','羊2','汽车']
times=1000*1000
first,change=0,0
for i in range(times):
    x=random.choice(a)
    y=random.choice(a)
    if x == y:
        first+=1
    else:
        change+=1
print("坚持自己选择获胜的概率：{:.4f};改变自己选择获胜的概率：{:.4f}".format(first/times,change/times))
