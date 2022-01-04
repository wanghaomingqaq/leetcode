# 解密犯罪时间 | 时间限制：1秒 | 内存限制：262144K | 语言限制：不限
# 警察在侦破一个案件时，得到了线人给出的可能犯罪时间，形如 “HH:MM” 表示的时刻。
# 根据警察和线人的约定，为了隐蔽，该时间是修改过的，解密规则为：利用当前出现过的数字，
# 构造下一个距离当前时间最近的时刻，则该时间为可能的犯罪时间。每个出现数字都可以被无限次使用。"
# "输入描述:
# 形如HH:SS的字符串，表示原始输入
# 输出描述:
# 形如HH:SS的字符串，表示推理出来的犯罪时间
# 示例1
# 输入
# 18:52
# 输出
# 18:55
# 说明
# 利用数字1, 8, 5, 2构造出来的最近时刻是18:55，是3分钟之后。结果不是18:51因为这个时刻是18小时52分钟之后。
# 示例2
# 输入
# 23:59
# 输出
# 22:22
# 说明
# 利用数字2, 3, 5, 9构造出来的最近时刻是22:22。 答案一定是第二天的某一时刻，所以选择可构造的最小时刻为犯罪时间。
# 备注:
#
# 可以保证线人给定的字符串一定是合法的。例如，“01:35” 和 “11:08” 是合法的，“1:35” 和 “11:8” 是不合法的。
# 最近的时刻有可能在第二天
#

import sys
time = sys.stdin.readline().strip()
times = [ int(x) for x in time if x!=":"]
H,M = [int(x) for x in time.split(":")]
print(times,H,M)
# 重点，列表中的组合数
num_time = list({i*10+j for i in times for j in times if i<6})
num_time.sort()
print(num_time)
if num_time[-1]>M:
    # 重点，当大于某个数，才输出
    for i in num_time:
        if i<=M:
            continue
        print(":".join([str(H),str(i)]))
else:
    print(":".join([str(num_time[0]),str(num_time[0])]))

# import sys
# time = sys.stdin.readline().strip().split(':')
# times = []
# for i in time:
#     for j in i:
#         times.append(j)
# times = [int(x) for x in times]
# print(times)
# time_shi = []
# for i in times:
#     if i <=6:
#         time_shi.append(i)
# new_min = max(time_shi)*10+max(times)
# if new_min>times[2]*10+times[3]:
#     print(times[0],times[1],new_min)
# a = [1,3,4,5,67,3,44,5,3,3]
# b = [str(x) for x in a if x <10 ]
# print(b)
# def decrypt_crime_time(s):
#     nums_list = [int(i) for i in s if i != ":"]
#     print(nums_list)
#     H, M = [int(i) for i in s.split(":")]
#     print(H,M)
#     nums_list = list({i * 10 + j for i in nums_list for j in nums_list if i <= 5})
#     print(nums_list)
#     nums_list.sort()
#     print("result:",nums_list)
#     if nums_list[-1]>M:
#         for i in nums_list:
#             if i <= M:
#                 continue
#             return ":".join([str(H), str(i)])
#     else:
#         return ":".join([str(nums_list[0]), str(nums_list[0])])
