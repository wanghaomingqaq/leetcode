'''
小明从糖果盒中随意抓一把糖果，每次小明会取出一半的糖果分给同学们。
当糖果不能平均分配时，小明可以选择从糖果盒中（假设盒中糖果足够）取出一个糖果或放回一个糖果。
小明最少需要多少次（取出、放回和平均分配均记一次），能将手中糖果分至只剩一颗

输入描述:
抓取的糖果数（<10000000000）：
15

输出描述:
最少分至一颗糖果的次数：
5
'''
import math
n = int(input())
x = n
count = 0
while x>1:
    if x%2:
        count = count+1
        if math.log2(x+1).is_integer() and math.log2(x-1).is_integer()==0:

            x = int((x+1)/2)
        elif math.log2(x-1).is_integer():
            x=int((x-1)/2)
        else:
            x = int((x-1)/2)
        count = count+1
    else:
        x = int(x/2)
        count=count+1
print(count)



