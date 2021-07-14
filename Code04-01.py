class Node() : # 데이터형, 붕어빵 틀
    def __init__(self):
        self.data = None
        self.link = None


node1 = Node() #붕어빵
node1.data = '다현'

node2 = Node()
node2.data = '정연'
node1.link = node2

node3 = Node()
node3.data = '쯔위'
node2.link = node3

node4 = Node()
node4.data = '사나'
node3.link = node4

node5 = Node()
node5.data = '지효'
node4.link = node5

# print(node1.data, end =' ')
# print(node1.link.data, end =' ')
# print(node1.link.link.data, end =' ')
# print(node1.link.link.link.data, end =' ')
# print(node1.link.link.link.link.data, end =' ')

# 노드 삽입
# newNode = Node()
# newNode.data = '재남'
# newNode.link = node2.link
# node2.link = newNode

# 노드 삭제 - 노드 3의 링크를 노드 2에 복사 후 노드 3의 데이터를 삭제
# node2.link = node3.link
# del(node3)


current = node1
print(current.data, end=' ')
while(current.link != None) :
    current = current.link
    print(current.data, end=' ')