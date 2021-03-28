def find_parent(team_list, node):
    if team_list[node] != node:
        team_list[node] = find_parent(team_list, team_list[node])   # 경로 압축 기법 (부모 노드만 저장)
    return team_list[node]


def union_team(team_list, a, b):
    a = find_parent(team_list, a)
    b = find_parent(team_list, b)
    if a < b:
        team_list[b] = a
    else:
        team_list[a] = b


n, m = map(int, input().split())
team_list = [0] * (n + 1)

for idx in range(n + 1):
    team_list[idx] = idx

for _ in range(m):
    judge, a, b = map(int, input().split())
    if judge == 0:
        union_team(team_list, a, b)
    elif judge == 1:
        if find_parent(team_list, a) == find_parent(team_list, b):
            print("YES")
        else:
            print("NO")
