import time
start_time = time.time()

# 생각나는대로 구현함

n,m = map(int, input().split())

# 2차원 리스트 만들기
cards = []
for i in range(n):
    cards.append(list(map(int, input().split())))
    cards[i].sort()


answer=0
min_list=[]
for j in range(n):
    tmp = min(cards[j])
    if tmp>answer:
        answer=tmp
        min_list.append(answer)

print(max(min_list))

end_time = time.time()
print("time: ", end_time - start_time)