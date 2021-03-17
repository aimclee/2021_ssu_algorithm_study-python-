n, m = map(int, input().split())
card_list = []

for _ in range(n):
    card_list.append(list(map(int, input().split())))

res = -2100000000
for cards in card_list:
    res = max(res, min(cards))

print(res)
