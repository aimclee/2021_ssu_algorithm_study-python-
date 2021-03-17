def is_validate_location(loc_x, loc_y, n):
    if 0 < loc_x <= n and 0 < loc_y <= n:
        return True
    else:
        return False


def move_left(cur, direction, n):
    if not is_validate_location(cur[0] + direction[0][0], cur[1] + direction[0][1], n):
        pass
    else:
        cur[0] = cur[0] + direction[0][0]
        cur[1] = cur[1] + direction[0][1]

    return cur


def move_right(cur, direction, n):
    if not is_validate_location(cur[0] + direction[1][0], cur[1] + direction[1][1], n):
        pass
    else:
        cur[0] = cur[0] + direction[1][0]
        cur[1] = cur[1] + direction[1][1]

    return cur


def move_up(cur, direction, n):
    if not is_validate_location(cur[0] + direction[2][0], cur[1] + direction[2][1], n):
        pass
    else:
        cur[0] = cur[0] + direction[2][0]
        cur[1] = cur[1] + direction[2][1]

    return cur


def move_down(cur, direction, n):
    if not is_validate_location(cur[0] + direction[3][0], cur[1] + direction[3][1], n):
        pass
    else:
        cur[0] = cur[0] + direction[3][0]
        cur[1] = cur[1] + direction[3][1]

    return cur


n = int(input())
input_dir = list(input().split())

direction = [[0, -1], [0, 1], [-1, 0], [1, 0]]    # L, R, U, D
cur = [1, 1]

for next_loc in input_dir:
    if next_loc == 'L':
        move_left(cur, direction, n)

    elif next_loc == 'R':
        move_right(cur, direction, n)

    elif next_loc == 'U':
        move_up(cur, direction, n)

    elif next_loc == 'D':
        move_down(cur, direction, n)

print(cur[0], cur[1])
