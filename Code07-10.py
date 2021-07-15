## 함수
def isQueuefull():
    global size, queue, front, rear
    if (rear+1)%size == front :
        return True
    else:
        return False

def enQueue(data):
    global size, queue, front, rear
    if isQueuefull() == True :
        print('큐 꽉!')
        return
    rear = (rear + 1) % size
    queue[rear] = data

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
    front = (front + 1) % size
    data = queue[front]
    queue[front] = None
    return data



## 변수
size = 5
queue = [None for _ in range(size)]
front, rear = 0, 0

## 메인
enQueue('화사'); enQueue('솔라'); enQueue('문별')
enQueue('휘인'); enQueue('유나')
print('출구<----',queue,'<--입구')
reData = deQueue(); print('다음 손님 :', reData)
print('출구<----',queue,'<--입구')
reData = deQueue(); print('다음 손님 :', reData)
print('출구<----',queue,'<--입구')
enQueue('재남'); enQueue('꼬북이')
print('출구<----',queue,'<--입구')
# reData = deQueue(); print('다음 손님 :', reData)
# reData = deQueue(); print('다음 손님 :', reData)
# print('출구<----',queue,'<--입구')
# enQueue('재남')
# print('출구<----',queue,'<--입구')
# enQueue('ㅋㅋ')
# print('출구<----',queue,'<--입구')
# enQueue('ㅁㄴ')
# reData = deQueue(); print('다음 손님 :', reData)
# reData = deQueue(); print('다음 손님 :', reData)
# print('출구<----',queue,'<--입구')
# reData = deQueue(); print('다음 손님 :', reData)
# reData = deQueue(); print('다음 손님 :', reData)