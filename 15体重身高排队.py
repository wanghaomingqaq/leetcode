# 假设有打乱顺序的一群人站成一个队列，
# 数组 people 表示队列中一些人的属性（不一定按顺序）。
# 每个 people[i] = [hi, ki] 表示第 i 个人的身高为 hi ，
# 前面 正好 有 ki 个身高大于或等于 hi 的人。
#
# 请你重新构造并返回输入数组people 所表示的队列。
# 返回的队列应该格式化为数组 queue ，其中 queue[j] = [hj, kj] 是队列中第 j 个人的属性
# （queue[0] 是排在队列前面的人）。
#
# 示例 1：
#
# 输入：people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
# 输出：[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
# 解释：
# 编号为 0 的人身高为 5 ，没有身高更高或者相同的人排在他前面。
# 编号为 1 的人身高为 7 ，没有身高更高或者相同的人排在他前面。
# 编号为 2 的人身高为 5 ，有 2 个身高更高或者相同的人排在他前面，即编号为 0 和 1 的人。
# 编号为 3 的人身高为 6 ，有 1 个身高更高或者相同的人排在他前面，即编号为 1 的人。
# 编号为 4 的人身高为 4 ，有 4 个身高更高或者相同的人排在他前面，即编号为 0、1、2、3 的人。
# 编号为 5 的人身高为 7 ，有 1 个身高更高或者相同的人排在他前面，即编号为 1 的人。
# 因此 [[5,0],[7,0],[5,2],[6,1],[4,4x],[7,1]] 是重新构造后的队列。
import sys

import pkg_resources

input = sys.stdin.readline().strip()
res = []
for i in input:
    if i.isdigit():
        res.append(i)
res = [int(x) for x in res]
high = [res[x] for x in range(len(res)) if x % 2 == 0]
index = [res[x] for x in range(len(res)) if x % 2 == 1]
double = list(zip(high,index))
double.sort(key=lambda x:(-x[0],x[1]))

print(double)
result = []
for people in double:
    result.insert(people[1],people)
print(result)
