# 给你一个整数 n（10 进制）和一个基数 k ，
# 请你将 n 从 10 进制表示转换为 k 进制表示，计算并返回转换后各位数字的 总和 。
#
# 转换后，各位数字应当视作是 10 进制数字，且它们的总和也应当按 10 进制表示返回。
#
#
# 示例 1：
#
# 输入：n = 34, k = 6
# 输出：9
# 解释：34 (10 进制) 在 6 进制下表示为 54 。5 + 4 = 9 。

n =34
k =6
high = int(n/k)
res = n%k
while high>0:
    res = res + high % k
    high = int(high/6)
print(res)

s = "ddsw2233"
for i in s:
    if i.isdigit():
        print(i)