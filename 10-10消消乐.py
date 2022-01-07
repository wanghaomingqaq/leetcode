'''
游戏规则：输入一个只包含英文字母的字符串，字符串中的两个字母如果相邻且相同，就可以消除。

在字符串上反复执行消除的动作，直到无法继续消除为止，此时游戏结束。

输出最终得到的字符串长度
'''
s = "bbbwwbbaaaaertsh"
s = list(map(str,s))
while True:
    count=0
    for i in range(1,len(s)):
        if s[i-1]==s[i]:
            s[i-1],s[i]="",""
        else:
            count = count+1
    s = [x for x in s if x!=""]
    if count>=len(s):
        break
print("".join(s))
