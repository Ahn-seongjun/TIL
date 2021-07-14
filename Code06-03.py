## 함수
def isstackfull():
    global  size, stack, top
    if top >= size-1 :
        return True
    else:
        return  False

def push(data):
    global size,stack,top
    if isstackfull()==True:
        print('꽉')
        return
    top +=1
    stack[top] = data

def isstackempty():
    global size,stack,top
    if top < 0:
        return True
    else:
        return False

def pop():
    global size, stack, top
    if isstackempty() ==False:
        data = stack[top]
        stack[top]=None
        top -=1
        a.append(data)
        print('팝!-->',data)
        return data

## 변수
size = 5
stack = [None for _ in range(size)]
top = -1
a=[]

push('커피1')
push('커피2')
print(stack)
pop()
print(stack)
push('커피3')
push('커피4')
print(stack)
pop()
print(stack)
push('커피5')
print(stack)
pop()
pop()
pop()
print(a)
## 메인