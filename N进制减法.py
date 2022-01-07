'''
实现一个基于字符串的N机制的减法。
需要对输入的两个字符串按照给定的N进制进行减法操作，输出正负符号和表示结果的字符串。

输入描述:
输入：三个参数。
第一个参数是整数形式的进制N值，N值范围为大于等于2、小于等于35。
第二个参数为被减数字符串；
第三个参数为减数字符串。有效的字符包括0~9以及小写字母a~z，字符串有效字符个数最大为100个字符，另外还有结尾的\0。
限制：
输入的被减数和减数，除了单独的0以外，不能是以0开头的字符串。
如果输入有异常或计算过程中有异常，此时应当输出-1表示错误。
输出描述:
输出：2个。
其一为减法计算的结果，-1表示出错，0表示结果为整数，1表示结果为负数。
其二为表示结果的字符串。

示例1:
输入
2 11 1
输出
0 10
说明
按二进制计算 11 -1 ，计算正常，0表示符号为正数，结果为10

示例2:
输入
8 07 1
输出
-1
说明
按8进制，检查到减数不符合非0前导的要求，返回结果为-1，没有其他结果内容。
'''
#

import sys
def ten_to_N(sum,N):
    high = sum
    low = sum%N
    res = [low]
    while high>1:
        high = int(high/N)
        low = high%N
        res.append(low)
    return res[::-1]
nums = ['2','111','100']
N = int(nums[0])
bj = nums[1]
j = nums[2]
if bj[0]=="0":
    fin = "-1"
else:
    bj_ten = int(bj,N)
    j_ten = int(j,N)
    sum = bj_ten-j_ten
    flag = 0
    if sum<0:
        sum=-sum
        flag = 1
    print(sum)
    res = ten_to_N(sum,N)
    s = []
    for x in res:
        if x>=10:
            s.append(chr(x+87))
        else:
            s.append(str(x))
    fin = "".join(s)
print(flag,fin)

# 10转N




