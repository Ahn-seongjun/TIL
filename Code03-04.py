## 함수 선언부(클래스 선언부)
# 추가
def add_data(friend) :
    katok.append(None) # 빈 칸 추가
    kLen= len(katok) # 배열의 길이
    katok[kLen-1]=friend
# 삽입
def insert_data(position, friend):
    katok.append(None)
    kLen = len(katok)

    for i in range(kLen-1,position,-1):
        katok[i] = katok[i-1]
        katok[i-1]=None

    katok[position]=friend
# 삭제
def delete_data(position) :
    kLen = len(katok)
    katok[position] = None
    for i in range(position+1,kLen):
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[kLen-1])
## 전역 변수부(선언)
katok = []
select = -1 # 1:추가, 2:삽입, 3:삭제, 4:종료

## 메인 코드부
if __name__ == '__main__' : # 메인 함수(진입점)
    while (select != 4) :
        select = int(input('선택 (1~4) -->'))

        if (select == 1):
            con = input("이름 :")
            add_data(con)
            print(katok)
        elif (select == 2):
            po = int(input('위치 :'))
            friend = input("이름 :")
            insert_data(po,friend)
            print(katok)
        elif (select == 3):
            num = int(input("위치 :"))
            delete_data(num)
            print(katok)
        elif (select == 4):
            print(katok)
            break
        else :
            print('1~4 중에 입력하세요')