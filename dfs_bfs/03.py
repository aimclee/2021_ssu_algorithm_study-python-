def is_validate_loc(x, y, n, m):
    if 0 <= x < n and 0 <= y < m:
        return True
    else:
        return False


# 아이스크림 범위 탐색 (BFS)
def search_area(queue, grid, dx, dy):
    while queue:
        cur_x = queue[0][0]
        cur_y = queue[0][1]

        queue.pop(0)
        for direction in range(4):
            next_x = cur_x + dx[direction]
            next_y = cur_y + dy[direction]

            if is_validate_loc(next_x, next_y, n, m) and grid[next_x][next_y] == 0:
                grid[next_x][next_y] = 1
                queue.append([next_x, next_y])


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
grid = []
queue = []
res = 0

# 맵 입력받기
for _ in range(n):
    grid.append(list(map(int, input())))

for x in range(n):
    for y in range(m):
        if grid[x][y] == 0:
            queue.append([x, y])
            grid[x][y] = 1
            search_area(queue, grid, dx, dy)
            res += 1

print(res)
