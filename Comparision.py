import os
filename = "南瓜1\Cmo_1f.txt."
size=1000000#根据实验需求更改大小
def mk_SubFile(srcName, sub, buf):
    [des_filename, extname] = os.path.splitext(srcName)
    filename = des_filename  + str(sub) + '.txt'
    print('正在生成子文件: %s' % filename)
    with open(filename, 'wb') as fout:
        #fout.writelines(s)
        fout.write(buf)
        return sub + 1

def split_By_size(filename, size):
    with open(filename, 'rb') as fin:
        buf = fin.read(size)
        sub = 1
        while len(buf) > 0:
            sub = mk_SubFile(filename, sub, buf)
            buf = fin.read(size)
    print("ok")


if __name__ == "__main__":
    split_By_size(filename, size)