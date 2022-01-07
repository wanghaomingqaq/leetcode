# 给定一个整数数组，找出总和最大的连续数列，并返回总和。
#
# 示例：
#
# 输入： [-2,1,-3,4,-1,2,1,-5,4]
# 输出： 6
# 解释： 连续子数组 [4,-1,2,1] 的和最大，为 6。

# 解题思路
# 动态规划：f(i) = max(f(i-1) + nums[i], nums[i])，其中f(i)表示截止到位置i且包含i的总和最大的连续数列和。
#
# 代码
#
class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]
        curr = nums[0]
        n = len(nums)
        for i in range(1, n):
            curr = max(curr + nums[i], nums[i])
            max_sum = max(max_sum, curr)
        return max_sum
#
# 作者：li-kuan
# 链接：https://leetcode-cn.com/problems/contiguous-sequence-lcci/solution/python-mian-shi-ti-1617-lian-xu-shu-lie-xc618/

import sys
nums = sys.stdin.readline().strip().strip("[").strip("]").split(",")
nums = list(map(int,nums))
res = Solution().maxSubArray(nums)
print(res)

#暴力法
# [-2,1,-3,4,-1,2,1,-5,4]
res = nums[0]
for i in range(len(nums)):
    sum_j = []
    for j in range(i,len(nums)):
        sum_j.append(nums[j])
        print(sum_j)
        res = max(sum(sum_j),res)
print(res)

