# 이코테 p149

# best practice : http://pythontutor.com/visualize.html#code=%23%20N,%20M%EC%9D%84%20%EA%B3%B5%EB%B0%B1%EC%9D%84%20%EA%B8%B0%EC%A4%80%EC%9C%BC%EB%A1%9C%20%EA%B5%AC%EB%B6%84%ED%95%98%EC%97%AC%20%EC%9E%85%EB%A0%A5%20%EB%B0%9B%EA%B8%B0%0An,%20m%20%3D%20map%28int,%20input%28%29.split%28%29%29%0A%0A%23%202%EC%B0%A8%EC%9B%90%20%EB%A6%AC%EC%8A%A4%ED%8A%B8%EC%9D%98%20%EB%A7%B5%20%EC%A0%95%EB%B3%B4%20%EC%9E%85%EB%A0%A5%20%EB%B0%9B%EA%B8%B0%0Agraph%20%3D%20%5B%5D%0Afor%20i%20in%20range%28n%29%3A%0A%20%20%20%20graph.append%28list%28map%28int,%20input%28%29%29%29%29%0A%0A%23%20DFS%EB%A1%9C%20%ED%8A%B9%EC%A0%95%ED%95%9C%20%EB%85%B8%EB%93%9C%EB%A5%BC%20%EB%B0%A9%EB%AC%B8%ED%95%9C%20%EB%92%A4%EC%97%90%20%EC%97%B0%EA%B2%B0%EB%90%9C%20%EB%AA%A8%EB%93%A0%20%EB%85%B8%EB%93%9C%EB%93%A4%EB%8F%84%20%EB%B0%A9%EB%AC%B8%0Adef%20dfs%28x,%20y%29%3A%0A%20%20%20%20%23%20%EC%A3%BC%EC%96%B4%EC%A7%84%20%EB%B2%94%EC%9C%84%EB%A5%BC%20%EB%B2%97%EC%96%B4%EB%82%98%EB%8A%94%20%EA%B2%BD%EC%9A%B0%EC%97%90%EB%8A%94%20%EC%A6%89%EC%8B%9C%20%EC%A2%85%EB%A3%8C%0A%20%20%20%20if%20x%20%3C%3D%20-1%20or%20x%20%3E%3D%20n%20or%20y%20%3C%3D%20-1%20or%20y%20%3E%3D%20m%3A%0A%20%20%20%20%20%20%20%20return%20False%0A%20%20%20%20%23%20%ED%98%84%EC%9E%AC%20%EB%85%B8%EB%93%9C%EB%A5%BC%20%EC%95%84%EC%A7%81%20%EB%B0%A9%EB%AC%B8%ED%95%98%EC%A7%80%20%EC%95%8A%EC%95%98%EB%8B%A4%EB%A9%B4%0A%20%20%20%20if%20graph%5Bx%5D%5By%5D%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20%23%20%ED%95%B4%EB%8B%B9%20%EB%85%B8%EB%93%9C%20%EB%B0%A9%EB%AC%B8%20%EC%B2%98%EB%A6%AC%0A%20%20%20%20%20%20%20%20graph%5Bx%5D%5By%5D%20%3D%201%0A%20%20%20%20%20%20%20%20%23%20%EC%83%81,%20%ED%95%98,%20%EC%A2%8C,%20%EC%9A%B0%EC%9D%98%20%EC%9C%84%EC%B9%98%EB%93%A4%EB%8F%84%20%EB%AA%A8%EB%91%90%20%EC%9E%AC%EA%B7%80%EC%A0%81%EC%9C%BC%EB%A1%9C%20%ED%98%B8%EC%B6%9C%0A%20%20%20%20%20%20%20%20dfs%28x%20-%201,%20y%29%0A%20%20%20%20%20%20%20%20dfs%28x,%20y%20-%201%29%0A%20%20%20%20%20%20%20%20dfs%28x%20%2B%201,%20y%29%0A%20%20%20%20%20%20%20%20dfs%28x,%20y%20%2B%201%29%0A%20%20%20%20%20%20%20%20return%20True%0A%20%20%20%20return%20False%0A%0A%23%20%EB%AA%A8%EB%93%A0%20%EB%85%B8%EB%93%9C%28%EC%9C%84%EC%B9%98%29%EC%97%90%20%EB%8C%80%ED%95%98%EC%97%AC%20%EC%9D%8C%EB%A3%8C%EC%88%98%20%EC%B1%84%EC%9A%B0%EA%B8%B0%0Aresult%20%3D%200%0Afor%20i%20in%20range%28n%29%3A%0A%20%20%20%20for%20j%20in%20range%28m%29%3A%0A%20%20%20%20%20%20%20%20%23%20%ED%98%84%EC%9E%AC%20%EC%9C%84%EC%B9%98%EC%97%90%EC%84%9C%20DFS%20%EC%88%98%ED%96%89%0A%20%20%20%20%20%20%20%20if%20dfs%28i,%20j%29%20%3D%3D%20True%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20result%20%2B%3D%201%0A%0Aprint%28result%29%20%23%20%EC%A0%95%EB%8B%B5%20%EC%B6%9C%EB%A0%A5&cumulative=false&curInstr=204&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%223%203%22,%22001%22,%22010%22,%22101%22%5D&textReferences=false
# dfs -> stack -> 재귀함수
# 아이디어는 비슷했는데, 조금 모자랐음.


import time
start_time = time.time()

# n은 행, m은 열
n,m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))
# print(graph) # [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]
# print(len(graph[0]) * len(graph)) # n*m의 값


visited = [[0]*m for _ in range(n)]
# print(visited) # [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

def search(r,c):
    ice_cream_num=0
    for _ in range(len(graph[0]) * len(graph)):

        # print(j)

        '''
        [0, 0, 1, 1, 0]
        [0, 0, 0, 1, 1]
        [1, 1, 1, 1, 1]
        [0, 0, 0, 0, 0]
        '''

        # 예외처리
        if r<=-1 or r>=n or c<=-1 or c>=m:
            continue
        
        # 이미 노드를 방문한 경우
        if visited[r][c] == 1:
            continue
            
        # 탐색을 진행하며 방문한 노드의 값이 0이면 숫자 0으로 반환. 
        if graph[r][c]==0:
            if visited[r][c]==0:
                visited[r][c] = 1
                search(r+1,c)
                search(r-1,c)
                search(r,c-1)
                search(r,c+1)
            ice_cream_num+=1
        elif graph[r][c] == 1:
            continue
    print(ice_cream_num)
        
search(0,0)


end_time = time.time()

print("time: ", end_time - start_time)