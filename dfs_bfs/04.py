def is_validate_loc(x, y, n, m):
    if 0 <= x < n and 0 <= y < m:
        return True
    else:
        return False


n, m = map(int, input().split())
gird = []
queue = [[0, 0]]
distance = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    gird.append(list(map(int, input())))

while queue:
    cur = queue.pop(0)

    if cur[0] == n - 1 and cur[1] == m - 1:
        print(distance[n - 1][m - 1] + 1)
        break

    for direction in range(4):
        next_x = cur[0] + dx[direction]
        next_y = cur[1] + dy[direction]

        if is_validate_loc(next_x, next_y, n, m) and distance[next_x][next_y] == 0:
            distance[next_x][next_y] = distance[cur[0]][cur[1]] + 1
            queue.append([next_x, next_y])

