'''
一辆运送快递的货车，运送的快递均放在大小不等的长方体快递盒中，
为了能够装载更多的快递，同时不能让货车超载，需要计算最多能装多少个快递。

输入描述:

第一行输入每个快递的重量，用英文逗号分隔，如：5,10,2,11

第二行输入货车的载重量，如：20

不需要考虑异常输入。

输出描述:

输出最多能装多少个快递，如：3
'''
# import sys
# lines = []
# for line in sys.stdin:
#     lines.append(line.strip())
# wight = list(map(int,lines[0].split(',')))
# car = lines[1]
wight = [5,10,2,11]
car = 20
print(wight,car)
wight.sort()
i,sum = 0,0
while sum<=car:
    sum = sum+wight[i]
    i = i + 1
print(i-1)