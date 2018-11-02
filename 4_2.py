g,d,e,f=0,0,0,0
zifu=input("请随意输入一串字符:")
for s in zifu:
    if ord('a')<=ord(s)<=ord('z')or ord('A')<= ord(s)<=  ord('Z'):
        g+=1
    elif ord('0')<=ord(s)<=ord('9'):
        d+=1
    elif ord(' ')==ord(s):
        e+=1
    else:
        f+=1
print("字母有{0}个,数字有{1}个,空格有{2}个,其他字符有{3}个".format(g,d,e,f))
