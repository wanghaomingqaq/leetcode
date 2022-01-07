'''
100个人围成一圈，每个人有一个编码，编号从1开始到100。
他们从1开始依次报数，报到为M的人自动退出圈圈，
然后下一个人接着从1开始报数，直到剩余的人数小于M。
请问最后剩余的人在原先的编号为多少？
'''
M = 7
res = [x for x in range(1,101)]
index = 0
while len(res)>=M:
    index =(index+M-1)%len(res)
    res.pop(index)

print(res)



