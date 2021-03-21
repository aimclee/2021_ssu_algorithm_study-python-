import time
start_time = time.time()

'''
망한코드

망한 이유 : 사고의 흐름을 그대로 코드로 나타내려고 하다가 결국 못풀었다.
이런 경우 dfs의 핵심적인 내용에 집중해보자.
(방문된 정점을 기록, 
방문이 안되어있는 노드를 탐색 + 간선이 존재하는지 여부, 
일반적으로 스택을 사용한다는 특징(재귀함수로 구현))
'''
n,m,v = map(int,input().split())

# 그래프 입력받기 
graph = []
for i in range(m):
    graph.append(list(map(int, input().split())))

# dfs 수행
duplicated_dfs =[]
dfs_list=[]
def dfs(v,graph,visited_dfs):
    
    
    # 그래프를 반복적으로 돌며 dfs 수행
    for i in range(n):
        j,k = graph[i]
        if j or k == v:
            visited_dfs[v-1] = True
            duplicated_dfs.append(graph[i])
            for a,b in duplicated_dfs:
                if a or b == v:
                    if v in duplicated_dfs:
                        duplicated_dfs.remove(v)
                        for c,d in duplicated_dfs:
                            if c>d:
                                dfs(d,graph, visited_dfs)
        dfs_list.append(d)                        


visited_dfs=[False]*n
# graph값 오름차순 sort

for i in range(n):
    graph[i].sort()
    

print(dfs(v,graph,visited_dfs))


end_time = time.time()
print("time: ", end_time - start_time)