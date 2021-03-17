n = int(input())
res = 0

for hour in range(0, n + 1):
    for minute in range(0, 60):
        for second in range(0, 60):
            time_str = str(hour) + str(minute) + str(second)
            if '3' in time_str:
                res += 1

print(res)
