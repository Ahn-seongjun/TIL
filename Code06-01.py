size = 5
stack = [None for _ in range(size)]
top = -1

top+=1
stack[top]= '커피'
top+=1
stack[top]= '녹차'
top+=1
stack[top]= '꿀물'

print('바닥 :',stack)

data = stack[top]
stack[top] = None
top -= 1
print('팝 -->', data)

print('바닥 :',stack)







size = 5
stack =[None for _ in range(size)]
top = -1

top += 1
stack[top] = '커피'
top += 1
stack[top] = '꿀물'
top += 1
stack[top] = '녹차'
print(stack)
print(data)

print("----------------------------------")
data = stack[top]
stack[top]=None
top -= 1
print(stack)
print(data)
data = stack[top]
stack[top]=None
top -= 1
print(stack)
print(data)
data = stack[top]
stack[top]=None
top -= 1
print(stack)
print(data)



