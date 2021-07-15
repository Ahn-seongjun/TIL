## 함수
def findMinIndex(ary):
    minIdx = 0
    for i in range(1, len(ary)):
        if ary[minIdx] > ary[i]:
            minIdx = i
    return minIdx
## 전역
import random
before = [ random.randint(10,99) for _ in range(20)]
after = []

testAry = [55,88,33,77]
## 메인
minPos = findMinIndex(testAry)
print('최솟값 -->',testAry[minPos])

print('정렬전 ->',before)
for _ in range(len(before)):
    minPos = findMinIndex(before)
    after.append(before[minPos])
    del(before[minPos])
print('정렬후 ->', after)