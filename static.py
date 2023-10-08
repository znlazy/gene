with open ("F://senquence dataset1(1000KB)/比对结果/result.txt",'r',encoding='utf-8')as f:
    count = 0
    consec_count = 0
    content=f.readlines()
    for line in content:
        for c in line:
            if c == '|':
                consec_count += 1
            else:
                if consec_count >= 30:
                    count += 1
                consec_count = 0
print("连续30个及以上的\"|\"字符，共有{}个".format(count))
