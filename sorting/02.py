n = int(input())
input_list = []

for _ in range(n):
    input_list.append(int(input()))

input_list.sort(reverse=True)
print(input_list)
