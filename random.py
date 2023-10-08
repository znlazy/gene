#线性同余法，种子数为513时产生的周期为928，随机性最好
def random1():
    global x0
    x0 = x0 * a + c   #线性同余法规则
    return int(x0 % m)

if __name__=='__main__':
    a=63
    c=10
    m=929
    x0 = int(input("请输入x0(0=<x0<m):"))#种子数
    r= []
    for i in range(0,999): #生成计算50次范围内
        r.append(random1())
        if r[0] == r[i]  and i!=0:
            print("周期:",i)
            break
        print(r[i])