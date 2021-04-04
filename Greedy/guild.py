n = int(input())
data = list(map(int, input().split()))
group = 0 # 모임의 개수
member = 0 # 모임 내 인원 수
data.sort()

for i in data:
    member += 1
    if member >= i:
        group += 1
        member = 0
        
print(group)
