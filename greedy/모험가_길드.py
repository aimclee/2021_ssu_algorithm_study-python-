import sys
input = sys.stdin.readline

n=int(input())

fear_degree = list(map(int, input().split()))
fear_degree.sort()

num_of_group = 0
cnt = 0

for i in fear_degree:
    cnt+=1
    if cnt >= i:
        num_of_group+=1
        cnt=0
print(num_of_group)