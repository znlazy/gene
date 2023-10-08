#!/usr/bin/env python
# -*- coding:utf-8 -*-
# TAGTCCGCATGGAAAGAAATATTGGGACGAAAAAATAAAAACTTGAGTCCGGGCGTCTCCGAGCGGTTCTTGTGGGAAAAAACTTTG
# def writeData(file):
#    # print("Loading raw data...")
#      raw_data = pd.read_csv(file, header=None,low_memory=False)
#      return raw_data
import pandas as pd
import numpy as np
from numpy import *
import copy
from matplotlib import pyplot as plt
from pandas import *
import sys
sys.setrecursionlimit(100000)
y=0
o=0
c=0
# 创建局部比对得分矩阵
def LocalScoreMatrix(m, n, w, replace, s, path, senquence1, senquence2, gap):
    for i in range(1, m):
        # 局部矩阵第一行及第一列均为0，不需要再初始化
        for j in range(1, n):
            # 获取最大值,与全局比对不同之处在于选取最大值时将0加入选择
            s[i][j] = max(0, s[i - 1][j - 1] + w[replace[senquence2[i - 1]]][replace[senquence1[j - 1]]],
                          s[i - 1][j] + gap, s[i][j - 1] + gap)
            # 记录最大值来的方向，若最大值为0则不必记录
            if s[i - 1][j - 1] + w[replace[senquence2[i - 1]]][replace[senquence1[j - 1]]] == s[i][j]:
                path[i, j, 2] = 1
            if s[i - 1][j] + gap == s[i][j]:
                path[i, j, 1] = 1
            if s[i][j - 1] + gap == s[i][j]:
                path[i, j, 0] = 1


# 寻找全局序列比对路径
def FindGlobalPath(i, j, path, OnePath, LastGlobalPath):
    # 递归终止条件：回到原点（0，0）
    if i == 0 and j == 0:
        OnePath.append((i, j))
        # 将OnePath进行深拷贝再加入至最终路径列表LastGlobalPath中
        LastGlobalPath.append(copy.deepcopy(OnePath))
        # 将该点出栈
        OnePath.pop()
    else:
        for k in range(3):
            # 判断每个点来的方向
            if path[i, j, k] == 1:
                # 下标0处记录从左来的方向
                if k == 0:
                    # 将该点入栈
                    OnePath.append((i, j))
                    # 进行递归记录下一个点
                    FindGlobalPath(i, j - 1, path, OnePath, LastGlobalPath)
                    # 递归返回后将该点出栈，记录另一方向
                    OnePath.pop()
                # 下标1处记录从上来的方向
                elif k == 1:
                    OnePath.append((i, j))
                    FindGlobalPath(i - 1, j, path, OnePath, LastGlobalPath)
                    OnePath.pop()
                # 下标2处记录从左上来的方向
                else:
                    OnePath.append((i, j))
                    FindGlobalPath(i - 1, j - 1, path, OnePath, LastGlobalPath)
                    OnePath.pop()


# 寻找局部序列比对路径
def FindLocalPath(i, j, path, OnePath, LastLocalPath):
    # 递归终止条件：某个没有记录方向的点!!!
    if all(path[i][j] == [0, 0, 0]):
        OnePath.append((i, j))
        # 将OnePath进行深拷贝再加入至最终路径列表LastLocalPath中
        LastLocalPath.append(copy.deepcopy(OnePath))
        # 将该点出栈
        OnePath.pop()
    else:
        for k in range(3):
            # 判断每个点来的方向
            if path[i, j, k] == 1:
                # 下标0处记录从左来的方向
                if k == 0:
                    # 将该点入栈
                    OnePath.append((i, j))
                    # 进行递归记录下一个点
                    FindLocalPath(i, j - 1, path, OnePath, LastLocalPath)
                    # 递归返回后将该点出栈，记录另一方向
                    OnePath.pop()
                # 下标1处记录从上来的方向
                elif k == 1:
                    OnePath.append((i, j))
                    FindLocalPath(i - 1, j, path, OnePath, LastLocalPath)
                    OnePath.pop()
                # 下标2处记录从左上来的方向
                else:
                    OnePath.append((i, j))
                    FindLocalPath(i - 1, j - 1, path, OnePath, LastLocalPath)
                    OnePath.pop()


# 输出比对后的序列
def ShowContrastResult(LastPath, senquence1, senquence2):
    # 依次输出每条路径
    #n=0
    #m=0
    for k, aPath in enumerate(LastPath):  # k为索引值，aPath为获得的键值
        rowS = ''
        colS = ''
        # 每条路径倒序遍历
        for i in range(len(aPath) - 1, 0, -1):
            # 方向从左边来
            if aPath[i][0] == aPath[i - 1][0]:
                rowS += senquence1[aPath[i - 1][1] - 1]
                #colS += '-'
                #n+=1
                #print("突变位置为：",senquence2.index(senquence2[aPath[i - 1][0] - 1]))
            # 方向从上面来
            elif aPath[i][1] == aPath[i - 1][1]:
                colS += senquence2[aPath[i - 1][0] - 1]
                #rowS += '-'
                #m+=1
                #print("突变位置为：",senquence1.index(senquence1[aPath[i - 1][1] - 1]))
            # 方向从左上来
            else:
                rowS += senquence1[aPath[i - 1][1] - 1]
                colS += senquence2[aPath[i - 1][0] - 1]

        #不是所有的最后一个基因都要被替换为*

        if len(colS)!=len(rowS):
            colS=list(colS)
            colS[-1]='*'
            cols=""
            for i in colS:
                cols+=i
        else:
            cols=colS
        Y=list()
        O=list()
        if colS == rowS:
            global o
            o+= 1
            O.append(o)
        for i in range(len(rowS)):
            if colS[i]!=rowS[i]:
                #print(f"这是第{m}组")
                print(f"突变位置为{i+1}")
                global y
                y+=1
                Y.append(y)


        # colS=str(cols)
        #return rowS
        #return n,m
        # 依次输出每条路的序列比对结果
        #print("======比对结果", k + 1, "======")
        # for i in range(len(Y)):
        #     if Y[i]==Y[i-1]:
        #         break
        #     else:
        #         print(f"突变数量为{y}")
        # for i in range(len(Y)):
        #     if Y[i]!=Y[i-1] :
        #         print(f"突变数量为：{Y[i]}")
        # for i in range(len(O)):
        #     if O[i]!=O[i-1]:
                #print(f"相同的数量为：{O[i]}")
        #print(f"相同的基因有{c}个")
        #print(f"突变数量为：{Y[i]}")
        #print(f"相同的数量为：{O[i]}")
        print(f"突变的数量为{y}")
        print(f"相同的数量为：{o}")
        print("序列1:", rowS)
        print("序列2:", cols)


# 判断是否为最终路径中的点
def judgePath(point, LastPath):
    for aPath in LastPath:
        if point in aPath:
            return True
    return False


#画出路径图
# def ShowPaths(senquence1, senquence2, LastPath):
#    # s1 = "0" + senquence1##列表类型与字符类型的相加减的
#     s1=senquence1
#     s2 = senquence2
#     # 列索引
#     col = list(s1)
#     # 行索引
#     row = list(s2)
#     # 设置画布大小
#     fig = plt.figure(figsize=(20, 20))
#     ax = fig.add_subplot(111, frameon=True, xticks=[], yticks=[], )
#     the_table = plt.table(cellText=s, rowLabels=row, colLabels=col, rowLoc='right',
#                           loc='center', cellLoc='bottom right', bbox=[0, 0, 1, 1])
#     # 设置表格文本字体大小
#     the_table.set_fontsize(8)
#     # 画出每个点的路径图
#     for i in range(m):
#         for j in range(n):
#             for k in range(3):
#                 if path[i, j, k] == 1:  # 画出记录的方向
#                     # 下标0处记录从左来的方向
#                     if k == 0:
#                         if judgePath((i, j), LastPath):  # 若某点在在最终路径中
#                             # 画出红色箭头
#                             plt.annotate('', xy=(j / n, (2 * m - 2 * i - 1) / (2 * (m + 1))),
#                                          xytext=((2 * j + 1) / (2 * n), (2 * m - 2 * i - 1) / (2 * (m + 1))),
#                                          arrowprops=dict(arrowstyle="->", color='r', connectionstyle="arc3"))
#                         else:
#                             # 未在最终路径中则画出黑色箭头
#                             plt.annotate('', xy=(j / n, (2 * m - 2 * i - 1) / (2 * (m + 1))),
#                                          xytext=((2 * j + 1) / (2 * n), (2 * m - 2 * i - 1) / (2 * (m + 1))),
#                                          arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
#                     # 下标1处记录从上来的方向
#                     elif k == 1:
#                         if judgePath((i, j), LastPath):
#                             plt.annotate('', xy=((2 * j + 1) / (2 * n), (2 * m - 2 * i - 1) / (2 * (m + 1))),
#                                          xytext=((2 * j + 1) / (2 * n), (m - i) / (m + 1)),
#                                          arrowprops=dict(arrowstyle="<-", color='r', connectionstyle="arc3"))
#                         else:
#                             plt.annotate('', xy=((2 * j + 1) / (2 * n), (2 * m - 2 * i - 1) / (2 * (m + 1))),
#                                          xytext=((2 * j + 1) / (2 * n), (m - i) / (m + 1)),
#                                          arrowprops=dict(arrowstyle="<-", connectionstyle="arc3"))
#                     # 下标1处记录从上来的方向
#                     elif k == 2:
#                         if judgePath((i, j), LastPath):
#                             plt.annotate('', xy=((2 * j + 1) / (2 * n), (2 * m - 2 * i - 1) / (2 * (m + 1))),
#                                          xytext=(j / n, (m - i) / (m + 1)),
#                                          arrowprops=dict(arrowstyle="<-", color='r', connectionstyle="arc3"))
#                         else:
#                             plt.annotate('', xy=((2 * j + 1) / (2 * n), (2 * m - 2 * i - 1) / (2 * (m + 1))),
#                                          xytext=(j / n, (m - i) / (m + 1)),
#                                          arrowprops=dict(arrowstyle="<-", connectionstyle="arc3"))
#     plt.show()
#

# 将碱基转换为集合下标
replace = {'A': 0, 'G': 1, 'C': 2, 'T': 3}
# 构造替换计分矩阵对数据集大小完全没有影响！！！
w = [[10, -1, -3, -4], [-1, 7, -5, -3], [-3, -5, 9, 0], [-4, -3, 0, 8]]
# 定义需要比对的序列

# senquence1=pd.read_csv('data1.txt',header=None)
# senquence2=pd.read_csv('data2.txt',header=None)
# senquence1 = input("请输入序列1：").upper()
# senquence2 = input("请输入序列2：").upper()
# 定义输入的gap
gap = int(input("请输入gap："))
choise = int(input("请选择要进行的序列比对(1-全局序列比对  2-局部序列比对) : "))

# if choise == 1:  # 进行全局序列比对
#     # 构建得分矩阵
#     GlobalScoreMatrix(m, n, w, replace, s, path, senquence1, senquence2, gap)
#     FindGlobalPath(m - 1, n - 1, path, OnePath, LastGlobalPath)
#     ShowContrastResult(LastGlobalPath, senquence1, senquence2)
#     ShowPaths(senquence1, senquence2, LastGlobalPath)
if choise ==2:  # 进行局部序列比对
    senquence2 = ''
    with open('data_2.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            senquence2 += line
            senquence2 = list(senquence2)
    senquence = ''
    senquence_ = list()
    with open('data_1.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            senquence += line
            senquence = list(senquence)
            l = len(senquence)
            print(l)
            t = int(l / 5)
            print(t)
            for i in range(0, l, 5):
                senquence_.append(senquence[i:i + 5])
            for i in range(0, t):
                global m
                m=i
                print(f"这是第{i+1}组")
                senquence1 = senquence_[i]
                print(senquence1)
                # 构建得分矩阵
                # 获取序列的长度
                m = len(senquence2) + 1
                n = len(senquence1) + 1
                # 构建m*n全0矩阵
                s = zeros((m, n))
                # 记录每个点的方向，下标0处存储从左来的方向，下标1处存储从上来的方向，下标2处存储从左上来的方向
                # 初始值均为0，若存在从某方向上来则将其对应下标的值置为1
                path = zeros((m, n, 3))
                # 记录每条路径
                OnePath = []
                # 记录所有全局序列比对路径
                LastGlobalPath = []
                # 记录所有局部序列比对路径
                LastLocalPath = []
                LocalScoreMatrix(m, n, w, replace, s, path, senquence1, senquence2, gap)
                row = where(s == np.max(s))[0]
                # 获取得分矩阵中最大值的列索引
                # for j in row:
                #     if j == '-':
                #         print("突变位置为：",senquence2.index(i))
                col = where(s == np.max(s))[1]
                #n=0
                for i in range(len(row)):  # 依次寻找不同局部比对的比对路径并输出比对结果
                    FindLocalPath(row[i], col[i], path, OnePath, LastLocalPath)
                    ShowContrastResult(LastLocalPath, senquence1, senquence2)

                    #print(f"突变数量为{n+m}")
                    #ShowPaths(senquence1, senquence2, LastLocalPath)#有bug,运行不出来
else:
    print("无效选择！")
