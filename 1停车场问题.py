#
# 问题：
# 特定大小的停车场，数组cars[ ]表示，其中0代表有车，1代表无车，
# 车辆大小不一，统计停车场最少可以停多少辆车，返回具体的数字。长度小于1000
#
# 输入：小车占一个车位（长度1），中车占两个车位（长度2），大车占三个车位（长度3）
# 输出：整形数字字符串，表示最少停车数目
#
# 输入：1，1，0，0，1，1，1，0，1
# 输出：3

import sys
input = sys.stdin.readline().strip().split("0")
cars = []
for car in input:
    if car != ' ':
        cars.append(car.strip())
s,m,l =0,0,0
for i in cars:
    lenth = i.count("1")
    if lenth>=3:
        l = l+ int(lenth/3)
        m = m+ int(lenth%3/2)
        s = s + lenth%3%2
    elif lenth==2:
        m = m+1
    elif lenth==1:
        s = s+1
sum = l+s+m
print(sum)


# s,m,l = 0,0,0
# for i in range(0,len(cars)-2):
#     flag_l = cars[i] and cars[i+1] and cars[i+2]
#     flag_m = cars[i] and cars[i+1]
#     if flag_l:
#         l = l+1
#     elif flag_m and flag_l==0:
#         m = m+1
# if car[-1] and car[-2]:
#     m = m+1
# m =l-m
# sum = cars.count(1)
# s = sum-m-l
# print(s,l,m)
