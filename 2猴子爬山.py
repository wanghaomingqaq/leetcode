# 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个n级的台阶总共有多少种跳法。

# 如果第一次跳的是1级台阶，那么剩下n-1级台阶，跳法是f(n-1)
# 如果第一次跳的是2级台阶，那么剩下n-2级台阶，跳法是f(n-2)
# 可以得出总跳法为: f(n) = f(n-1) + f(n-2)

n = int(input())
def numWays(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:   
        return numWays(n-1)+numWays(n-2)
print(numWays(n))