# 선형리스트의 원리_데이터 삽입

katok =['다현', '정연', '쯔위', '사나', '지효', '모모']

def insert_data(position, friend):
    katok.append(None)
    kLen = len(katok)

    for i in range(kLen-1,position,-1):
        katok[i] = katok[i-1]
        katok[i-1]=None

    katok[position]=friend

print(katok)
insert_data(3,'미나')
print(katok)