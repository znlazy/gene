
with open('Cmo_20.txt','r',encoding='utf-8') as f:
    with open('Cmo_20f.txt','w',encoding='utf-8') as f1:
        content=f.readlines()
        for line in content:
            #print(line)
            #print("这是一行")
            for i in line:
                if i !='N' and i!='n':
                    f1.write(i)
f1.close()
f.close()
