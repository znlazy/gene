import sys
sys.setrecursionlimit(1000000000)
file1 = open("南瓜1/Cmo_1f.txt1.txt")
file2 = open("西葫芦1/Cma_1f.txt1.txt")
while True:
    s1 = file1.readline()
    s2 = file2.readline()

    # 判断是否读取到内容
    if not s1:
        break
    # 每读取一行的末尾已经有了一个 `\n    m, n = len(s1), len(s2)
    m, n = len(s1), len(s2)
    dp = [[0] * n for _ in range(m)]
    max_len = 0
    max_end = 0
    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    max_end = i
            else:
                dp[i][j] = 0
    print(s1[max_end - max_len + 1:max_end + 1],end='\n')
    print(end='\n')
file1.close()
file2.close()