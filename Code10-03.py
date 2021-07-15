# 숫자 더하기
def addNumber(num):
    if num == 1:
        return 1
    return num + addNumber(num-1)

print(addNumber(10))

# 팩토리얼 구하기

def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)

print(factorial(5))

# 재귀호출

def recu(num):
    if num==1:
        return 1
    print("%d*%d! 호출"%(num,num-1))
    print(num*factorial(num-1))
    recu(num-1)
recu(5)

# 카운트 다운
def countdown(num):
    if num == 0:
        print('발사!')
    else :
        print(num)
        countdown(num-1)
countdown(10)

# 별 모양 출력
def starshape(num):
    if num >0 :
        starshape(num-1)
        print("*" * num)

starshape(5)