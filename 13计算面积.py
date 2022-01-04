# [计算面积]
#
# 绘图机器的绘图笔初始位i在原点(0.0)。 机器启动后其绘图笔按下面规则绘制直线:
#
# 1 )尝试沿着横向坐标轴正向绘制直线，直到给定的终点值E,
#
# 2 )期间可通过指令在纵坐标轴方向进行偏移。井同时恰制直线，偏移后按规则1绘制直线;指令的格式为X offsetY。
# 表示在横坐标X沿纵坐标方向偏移, offset为正数表示正向偏移,为负数表示负向偏移。
#
# 给定了横坐标格点值E.以及若干条检制指令。请计算给制的直线和横坐标轴。以及X-E的直线组成图形的面积。
#
# 输入模述:
#
# 首行为两个整数N,E。表示有N条指令。机器运行的横坐标終点值E.
#
# 接下来N行。每行两个整数表示-条给制指令x offsetY。用例保证横坐标X以递增排序方式出现。且不会出现相同横坐标义。取值范围:0<Nc= 1000.00 X<= E <20000.10000 < oter如1000.
#
# 输出描述:
#
# 一个整数，表示计算得到的面积。用例保证.结果范围在0-4294967295内
#
# 示例1:
#
# 输入
#
# 4 10
#
# 1 1
#
# 2 1
#
# 3 1
#
# 4 -2
#
# 输出
#
# 12

import sys
lines = []
for line in sys.stdin:
    new = line.strip().split()
    inner = list(map(int, new))
    lines.append(inner)
N,E = lines[0][0],lines[0][1]
lines.pop(0)
print(lines,N,E)
y=0
sum = 0
for i in range(1,len(lines)):
    y = y+lines[i-1][1]
    x = lines[i][0]-lines[i-1][0]
    sum = sum + x*y
    print("reslt",x,y,sum)
y = y+lines[-1][1]
sum=sum +y*(E-lines[-1][0])
print(sum)

