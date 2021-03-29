# 전략: 최소 인원에 따라 그룹을 만들어주기
n = int(input())
adventurer_list = list(map(int, input().split()))

adventurer_list.sort(reverse=True)
res = 0
cnt = 1
num = adventurer_list.pop()
while adventurer_list:
    if cnt == num:
        cnt = 1
        res += 1
        num = adventurer_list.pop()
    else:
        cnt += 1
        adventurer_list.pop()

print(res)
