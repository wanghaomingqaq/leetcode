# 给你一个字符串 word ，该字符串由数字和小写英文字母组成。
#
# 请你用空格替换每个不是数字的字符。例如，"a123bc34d8ef34" 将会变成 " 123 34 8 34" 。
# 注意，剩下的这些整数为（相邻彼此至少有一个空格隔开）："123"、"34"、"8" 和 "34" 。
#
# 返回对 word 完成替换后形成的 不同 整数的数目。
#
# 只有当两个整数的 不含前导零 的十进制表示不同， 才认为这两个整数也不同。
#
# 示例 1：
# 输入：word = "a123bc34d8ef34"
# 输出：3
# 解释：不同的整数有 "123"、"34" 和 "8" 。注意，"34" 只计数一次。
s = "leet1234code123asfd23"
res = []
sum = 0
for i in range(len(s)):
    if s[i].isalpha():

        sum = 0
    else:
        sum = sum*10+int(s[i])
        if i< len(s)-1 and s[i+1].isalpha():
            res.append(sum)
        if i == len(s)-1:
            res.append(sum)

print(res)

# 正则切割
import re
res = re.split(r'[a-z]+',s)
res = [int(x) for x in res if x!='']
print(len(set(res)))