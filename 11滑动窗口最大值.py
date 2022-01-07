# 给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
#
# 示例:
#
# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7]
# 解释:
#
#   滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# import sys
# lines = []
# for line in sys.stdin:
#     lines.append(line.strip())
# nums = lines[0]
# k = int(lines[1])
nums = [1,3,-1,-3,5,3,6,7]
k = 3
res = []
for i in range(len(nums)-k+1):
    tmp = max(nums[i:i+k])
    res.append(tmp)
print(res)
