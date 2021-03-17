# elapsed time : 1.1597399711608887

import time

start_time = time.time()

input_data = input()
row = int(input_data[1]) - 1
col = int(ord(input_data[0])) - int(ord('a'))

result = 0
steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, -1), (2, 1), (1, -2), (1, 2)] # 이동 가능한 경우의 수

for step in steps:
    mov_row = row + step[0]
    mov_col = col + step[1]
    if mov_row>=0 and mov_row<8 and mov_col>=0 and mov_col<8:
        result+=1
        
print(result)
end_time = time.time()

print("elapsed time : ", end_time-start_time)
