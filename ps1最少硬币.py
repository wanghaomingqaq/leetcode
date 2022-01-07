# 给定不同面额的硬币 coins 和一个总金额 amount。
# 编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
# 如果没有任何一种硬币组合能组成总金额，返回-1。
# 你可以认为每种硬币的数量是无限的。
#
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3
# 解释：11 = 5 + 5 + 1
coins = [2, 5]
amount = 3
dp = [amount + 1] * (amount + 1)
print(dp)
# f[i]=min(f[i-coin]+1，...f[i-coin]+1)
tmp = 0
# def mincoin(coins, amount):
#     for i in coins:
#         tmp = min()
#     return re

class Solution:
    # 动态规划, 完全背包问题, 无界背包问题
    # # 时间复杂度：O(ntk)， 空间复杂度：O(t), n是币种种类, t是目标总额, k是某种币种凑出总额t的硬币数
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     dp = [amount + 1] * (amount + 1)
    #     dp[0] = 0
    #     for coin in coins:
    #         for j in range(amount, 0, -1):
    #             res = j // coin + 1
    #             for k in range(1, res):
    #                 dp[j] = min(dp[j], dp[j - k * coin] + k)
    #     return -1 if dp[amount] > amount else dp[amount]

    # 时间复杂度：O(nt)， 空间复杂度：O(t), n是币种种类, t是目标总额, 空间优化, 类似于贪心算法
    def coinChange(self, coins, amount):
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return -1 if dp[amount] > amount else dp[amount]


res =Solution().coinChange(coins, amount)
print(res)
