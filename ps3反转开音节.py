'''
相对开音节构成的结构为辅音+元音(aeiou)+辅音(r除外)+e
常见的单词有bike cake 给定一个字符串，以空格为分隔符 反转每个单词的字母
若单词中包含如数字等其他非字母时不进行反转 反转后计算其中含有相对开音节结构
的子串个数 (连续子串中部分字符可以重复)

输入描述 字符串 以空格分割的多个单词 长度<10000 字母只考虑小写

输出描述 含有相对开音节结构的子串个数

示例1： 输入 ekam a ekac 输出 2 说明： 反转后为 make a cake
其中make和cake为相对开音节子串 返回2 示例2： 输入 !ekam a ekekac 输出 2
说明 反转后为 !ekam a cakeke 因为!ekam含有非英文字母，所以未反转
其中 cake和keke 为相对开音节子串 返回2

'''
import sys
str = sys.stdin.readline().strip().split()
print(str)
k = ['a','e','i','o','u']
def is_k(str):
    if str[0] not in k and str[-1]=='e' and str[1] in k and str[2] not in k and str[2]!=' r':
       return True
    else:
        return False
res = []
for s in str:
    for i in range(len(s)):
        if s[i].isalpha()==0:
            res.append(s)
            break
        elif s[i].isalpha() and i == len(s)-1:
            res.append(s[::-1])
count = 0
for r in res:
    for j in range(len(r)):
        if len(r)<4:
            break
        m = r[j:j+4]
        if len(m)<4:
            break
        if is_k(m):
            count = count+1
print(res,count)


print(is_k('make'))
