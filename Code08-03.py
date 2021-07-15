## 함수, 클래스
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

## 전역변수
root = None
memory = []
# 실무는 nameAry 대신 DB의 대용량 데이터, 크롤링한 데이터
nameAry = ['블랙핑크', '레드벨벳', '에이핑크', '걸스데이', '트와이스', '마마무']

import  random
numberAry = [random.randint(100000,999999) for _ in range(500)]
numberAry.insert(5,3000000)
print(numberAry)
## 메인
# 첫 노드(=root) 만들기

node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)

# 나머지 노드들 자리잡기
for name in nameAry[1:]:
    node = TreeNode()
    node.data = name

    current = root
    while True :
        if name < current.data :
            if current.left == None :
                current.left = node
                break
            current = current.left
        else :
            if current.right == None :
                current.right = node
                break
            current = current.right

    memory.append(node)

print('이진탐색트리')

findData = '바마무'

current = root
while True :
    if current.data == findData :
        print(findData,'찾았어요. ^^')
        break
    elif findData < current.data:
        if current.left == None:
            print(findData,'없어요 ㅠㅠ')
            break
        current = current.left
    else:
        if current.right == None:
            print(findData,'없어요 ㅠㅠ')
            break
        current = current.right


# 첫 노드(=root) 만들기

node = TreeNode()
node.data = numberAry[0]
root = node
memory.append(node)

# 나머지 노드들 자리잡기
for name in numberAry[1:]:
    node = TreeNode()
    node.data = name

    current = root
    while True :
        if name < current.data :
            if current.left == None :
                current.left = node
                break
            current = current.left
        else :
            if current.right == None :
                current.right = node
                break
            current = current.right

    memory.append(node)

print('이진탐색트리')

findData = 3000000

current = root
while True :
    if current.data == findData :
        print(findData,'찾았어요. ^^')
        break
    elif findData < current.data:
        if current.left == None:
            print(findData,'없어요 ㅠㅠ')
            break
        current = current.left
    else:
        if current.right == None:
            print(findData,'없어요 ㅠㅠ')
            break
        current = current.right