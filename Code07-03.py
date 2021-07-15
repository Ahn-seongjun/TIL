## 함수
# def isQueuefull():
#     global size, queue, front, rear
#     if rear >= size-1 :
#         return True
#     else:
#         return False
def isQueuefull():
    global size, queue, front, rear
    if rear !=size-1:
        return False
    elif rear == size-1 and front == -1 :
        return True
    else:
        for i in range(front + 1, size):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False

def isQueueEmpty():
    global size, queue, front, rear
    if front == rear:
        return True
    else:
        return False

def deQueue():
    global size, queue, front, rear
    if isQueueEmpty() == True:
        print('큐 텅!')
        return  None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def enQueue(data):
    global size, queue, front, rear
    if isQueuefull() == True :
        print('큐 꽉!')
    else :
        rear += 1
        queue[rear] = data

## 변수
size = 5
queue = [None for _ in range(size)]
front, rear = -1, -1

## 메인
enQueue('화사'); enQueue('솔라'); enQueue('문별')
enQueue('휘인'); enQueue('유나')
print('출구<----',queue,'<--입구')
reData = deQueue(); print('다음 손님 :', reData)
reData = deQueue(); print('다음 손님 :', reData)
print('출구<----',queue,'<--입구')
enQueue('재남')
print('출구<----',queue,'<--입구')
enQueue('ㅋㅋ')
print('출구<----',queue,'<--입구')
enQueue('ㅁㄴ')
# reData = deQueue(); print('다음 손님 :', reData)
# reData = deQueue(); print('다음 손님 :', reData)
# print('출구<----',queue,'<--입구')
# reData = deQueue(); print('다음 손님 :', reData)
# reData = deQueue(); print('다음 손님 :', reData)