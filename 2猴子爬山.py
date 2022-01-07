# 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个n级的台阶总共有多少种跳法。

# 如果第一次跳的是1级台阶，那么剩下n-1级台阶，跳法是f(n-1)
# 如果第一次跳的是2级台阶，那么剩下n-2级台阶，跳法是f(n-2)
# 可以得出总跳法为: f(n) = f(n-1) + f(n-2)

# 递归
n = int(input())
def numWays(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:   
        return numWays(n-1)+numWays(n-2)
print(numWays(n))

#动态规划ss
# a,b = 1,1
# for i in range(n):
#     a,b = b,a+b
# print(a)
dp = [n+1]*(n+1)
dp[0]=1
dp[1]=1
for i in range(2,n+1):
    dp[i] = dp[i-1]+dp[i-2]
print(dp[-1])