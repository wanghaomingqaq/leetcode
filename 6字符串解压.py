# 现在有一种字符串的压缩规则是这样的：
# k[string]，表示string连续出现k 次（0 < k < 1000）。
# 比如：s = "ef3[a]2[bc]gh", 解压后的字符串为："efaaabcbcgh"，
# 这种压缩也可以相互嵌套：s = "3[a2[c]]", 解压后为："accaccacc"。
#
# 输入一个压缩的字符串s，请输出解压后的字符串。
# 输入都是严格合法的，数字只用来表示重复次数，不会出现3a 或者2[4]这样的输入。
# 解压后的字符串只有字母。
import sys

input_str = sys.stdin.readline().strip()
stack, res, cnt = [], "", 0
for s in input_str:
    if cnt == 0:
        if s == "[":
            stack.append(s)
            cnt = cnt + 1
        else:
            res = res + s
        continue
    if cnt>0:
        if s=="[":
            stack.append(s)
            cnt = cnt+1
        elif s=="]":
            cnt =cnt-1
            tmp = stack.pop()
            while tmp[0]!="[":
                tmp = stack.pop()+tmp
            tmp = tmp[1:]
            print(tmp)
            if cnt==0:
                n = int(res[-1])
                res = res[:-1]
                res = res+tmp*n
            else:
                stack.append(tmp*int(stack.pop()))
        else:
            stack.append(s)
print(res)
# 3[a2[c]]
# res = []
# index_l = input_str.find("[")
# index_r = input_str.find("]")
# for i in range(len(input_str)):
#     if input_str[i]=="[":
#         res.append(input_str[:i - 1])
#         for j in range(i,len(input_str)):
#             if input_str[j] == "]":
#                 res.append(int(input_str[i-1])*input_str[i+1:j])
#
# res.append(input_str[:index_l-1])
# res.append(input_str[index_l+1:index_r]*int(input_str[index_l-1]))
# print("".join(res))
# print(index_l,index_r)
# for s in input_str:
#     if s == "[":
#         s.find()
#         res.append()
#
# class Solution:
#     def unZipString(self, S):
#         res, stack, cnt = '', [], 0
#
#         for s in S:
#
#             if cnt == 0:  # 没有出现括号的情况，直接输出
#                 if s != '[':
#                     res += s
#                 else:
#                     stack.append(s)
#                     cnt += 1
#                 continue #
#
#             if cnt > 0:   # 有括号的情况
#                 if s == '[':
#                     stack.append(s)
#                     cnt += 1
#                 elif s == ']':  # 此时要出栈
#                     cnt -= 1
#                     tmp = stack.pop()
#                     while tmp[0] != '[':
#                         tmp = stack.pop() + tmp
#
#                     tmp = tmp[1:]  # 把第一个字符去掉
#
#                     if cnt == 0:
#                         n = int(res[-1])
#                         res = res[:-1]
#                         res += n * tmp
#                     else:
#                         n = int(stack.pop())
#                         stack.append(n * tmp)
#                 else:  # 其他情况
#                     stack.append(s)
#
#         return res
#
#
#
# if __name__ == '__main__':
#     solu = Solution()
#     S = '2[3[a]bb2[c]]'
#     # S = '3[a2[c]]'
#     print(solu.unZipString(S))
