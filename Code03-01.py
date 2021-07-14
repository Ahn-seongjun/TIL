# 카톡으로 연락온 친구들 배열 저장
katok = [] # 빈 배열

def add_data(friend) :
    katok.append(None) # 빈 칸 추가
    kLen= len(katok) # 배열의 길이
    katok[kLen-1]=friend

add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')

print(katok)

# katok.append('다현')
# katok.append('정연')
# katok.append('쯔위')
#
# print(katok)