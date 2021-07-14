## 함수
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

## 전역
memory = []
head, current, pre = None, None, None
dataArray = ['다현','정연','쯔위','사나','지효'] # 어떤 데이터든 관계없음

## 메인
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


printNode(head)
insertNode('다현','화사')
printNode(head)
insertNode('사나','솔라')
printNode(head)
insertNode('재남','문별')
printNode(head)

deleteNode('화사')
printNode(head)
deleteNode('쯔위')
printNode(head)
deleteNode('재남')
printNode(head)