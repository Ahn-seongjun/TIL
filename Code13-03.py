## 함수
def binSearch(ary,data):
    pos = -1
    start = 0
    end = len(ary) -1
    while start <= end :
        mid = (start + end) // 2
        if data == ary[mid] :
            return mid
        elif data > ary[mid]:
            start = mid + 1
        else :
            end = mid - 1
    return  pos


## 변수
dataAry = [50,60,105,120,150,160,162,168,177,188]
findData = 162

## 메인

print('배열 -->', dataAry)
position = binSearch(dataAry,findData) # -1
print(position)
if position == -1:
    print('못찾음..')
else:
    print(findData, '는', position, '위치에 있음')