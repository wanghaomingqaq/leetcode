'''
给定一个非空字符串S，其被N个‘-’分隔成N+1的子串，给定正整数K，
要求除第一个子串外，其余的子串每K个字符组成新的子串，并用‘-’分隔。
对于新组成的每一个子串，如果它含有的小写字母比大写字母多，
则将这个子串的所有大写字母转换为小写字母；反之，如果它含有的大写字母比小写字母多，
则将这个子串的所有小写字母转换为大写字母；大小写字母的数量相等时，不做转换。

输入描述:

输入为两行，第一行为参数K，第二行为字符串S。

输出描述:

输出转换后的字符串。

示例1

输入
3

12abc-abCABc-4aB@
输出

12abc-abc-ABC-4aB-@
'''
def rev(str):
    count_s,count_b = 0,0
    for s in str:
        if s.islower():
            count_s=count_s+1
        elif s.isupper():
            count_b = count_b+1
        else:
            continue
    if count_s>count_b:
        return str.lower()
    elif count_s<count_b:
        return str.upper()
    else:
        return str

s = "12abc-abCABc-4aB@"
nums =s.split("-")
new = nums[0]
new = rev(new)
tmp = "".join(nums[1:])
after = []
for i in range(0,len(tmp),3):
    t = tmp[i:i+3]
    t = rev(t)
    after.append(t)
new = new+ "-"+"-".join(after)
print(new)
