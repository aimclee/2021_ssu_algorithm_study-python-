def find_parent(house_list, node):
    if house_list[node] != node:
        house_list[node] = find_parent(house_list, house_list[node])
    return house_list[node]


def union_home(house_list, a, b):
    a = find_parent(house_list, a)
    b = find_parent(house_list, b)
    if a < b:
        house_list[b] = a
    else:
        house_list[a] = b


v, e = map(int, input().split())
house_graph = [0] * (v + 1)

house_list = []
res = 0

for idx in range(1, v + 1):
    house_graph[idx] = idx

for _ in range(e):
    a, b, cost = map(int, input().split())
    house_list.append((cost, a, b))

house_list.sort()
last = 0

for house in house_list:
    cost, a, b = house
    if find_parent(house_graph, a) != find_parent(house_graph, b):
        union_home(house_graph, a, b)
        res += cost
        last = cost

print(res - last)
