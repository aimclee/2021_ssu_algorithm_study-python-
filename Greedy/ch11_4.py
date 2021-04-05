#만들 수 없는 금액
n = int(input())
coin = list(map(int,input().split()))
coin.sort()
res=0
cnt=1

for i in coin:
    if res > i:
        print(cnt)
        break
    cnt += i