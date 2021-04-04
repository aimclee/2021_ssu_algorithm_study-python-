# 같은 무게의 공 다른 공으로 취급하는 경우, 조합 : (3, 1)와 (1, 3) 동일하게 취급

n, m = map(int, input().split())
data = list(map(int, input().split()))
sets = []
for i in range(len(data)):
    for j in range(i+1, len(data)):
        if data[i]!=data[j]:
            sets.append((data[i], data[j]))
        
result = len(sets)
print(result)
