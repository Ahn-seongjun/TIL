## 함수
def selectionSort(ary):
    n = len(ary)
    for i in range(0, n-1):
        minIdx = i
        for k in range(i+1,n):
            if ary[minIdx] > ary[k]:
                minIdx = k
        ary[i], ary[minIdx] = ary[minIdx], ary[i]

    return ary
## 전역
import random
dataAry = [random.randint(10,99) for _ in range(20)]

## 메인
print('정렬전 ->',dataAry)
dataAry = selectionSort(dataAry)
print('정렬후 ->', dataAry)

########################################################
def Dsort(ary):
    n = len(ary)
    for i in range(0,n-1):
        midx = i
        for k in range(i+1,n):
            if ary[midx] > ary[k]:
                midx = k
        ary[i], ary[midx] = ary[midx], ary[i]
    return ary

DA =[random.randint(0,99) for _ in range(15)]

print(DA)
Dsort(DA)
print(DA)