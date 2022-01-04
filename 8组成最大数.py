# 给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
# 注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
#
# 示例 1：
#
# 输入：nums = [10,2]
# 输出："210"
#
# 输入：nums = [3,30,34,5,9]
# 输出："9534330"
# 示例 3：
#
# 输入：nums = [1]
# 输出："1"
# 示例 4：
#
# 输入：nums = [10]
# 输出："10"
# [3,30,34,5,9]
import sys
from functools import cmp_to_key


def cmp(a, b):
    str1 = str(a) + str(b)
    str2 = str(b) + str(a)
    if str1 > str2:
        return -1  # 不换序
    elif str1 < str2:
        return 1  # 换序
    else:
        return 0


nums = sys.stdin.readline().strip().strip("[").strip("]").split(",")
nums.sort(key=cmp_to_key(cmp))
res = "".join(nums)
print(res)


# [3,30,34,5,9]
# class Solution(object):
#     def largestNumber(self, nums):
#         # 正数时，按照列表本身的顺序排列； 负数时，按照列表本身顺序的逆序排序  # lambda表达式<0时,也就是303<330,返回-1,反过来排序
#         nums.sort(key=cmp_to_key(cmp))
#         res = ''.join(nums)
#         return res
#
#
# nums = sys.stdin.readline().strip().strip("[").strip("]").split(",")
# result = Solution().largestNumber(nums)
# print(result)
# nums.sort(key=lambda x:(x[0]),reverse=True)
# print(nums)
# res = []
# for i in range(len(nums)-1):
#     if nums[i+1][0]==nums[i][0]:
#         pass
#     else:
#         res.append(nums[i])
# print(res)


#
# print(nums)
# high_index = [int(x[0]) for x in nums]
# high_index.sort()
#
# print(high_index)
# print(num)
# for i in num:
#     pass
