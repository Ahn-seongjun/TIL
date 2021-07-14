# 선형 리스트를 1.추가, 2.삽입, 3.삭제, 4.종료 코드를
# ---> 연결리스트에 적용하기
## 함수 선언부(클래스 선언부)
class Node() : # 데이터형, 붕어빵 틀
    def __init__(self):
        self.data = None
        self.link = None

def printNode(start):
    current = start
    print(current.data, end=' ')
    while(current.link != None) :
        current = current.link
        print(current.data, end=' ')
    print()


def insertNode(findData, insertData):
    global memory, head, current, pre

    # 첫 노드 앞에 삽입
    if findData == head.data :
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return

    # 중간 노드 앞에 삽입
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
    # 마지막 노드에 추가할 때
    node = Node()
    node.data = insertData
    current.link = node
    return

def deleteNode(deleteData):
    global  memory, head, current, pre
    # 첫 노드 삭제
    if head.data == deleteData:
        current = head
        head = head.link
        del(current)
        return
    # 그외 노드 삭제
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return
    # 삭제할 노드 못찾음
    return

## 전역 변수부(선언)
memory = []
head, current, pre = None, None, None
dataArray = ['다현','정연','쯔위','사나','지효'] # 어떤 데이터든 관계없음
select = -1 # 1:추가, 2:삽입, 3:삭제, 4:종료

## 메인 코드부
# 첫데이터를 노드로 만들기
node = Node() # 빈 노드 생성
node.data = dataArray[0]
head = node
memory.append(node)

for data in dataArray[1:] : #['정연'....]
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

if __name__ == '__main__' : # 메인 함수(진입점)
    while (select != 4) :
        select = int(input('선택 (1~4) -->'))

        if (select == 1):
            printNode(head)
        elif (select == 2):
            fin = input('찾는 이름 :')
            inser = input("넣을 이름 :")
            insertNode(fin, inser)
            printNode(head)
        elif (select == 3):
            dele = input("삭제 이름 :")
            deleteNode(dele)
            printNode(head)
        elif (select == 4):
            printNode(head)
            break
        else :
            print('1~4 중에 입력하세요')
