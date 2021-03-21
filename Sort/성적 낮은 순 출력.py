import time

# elapsed time : 6.796998739242554

num = int(input())
stu_data = []

start_time = time.time()

# 함수 이용
def score(data):
    return data[1]

for _ in range(num):
    input_data = input().split()
    stu_data.append((input_data[0], input_data[1]))

stu_data = sorted(stu_data, key = score)

for stu in stu_data:
    print(stu[0], end=' ')
    
print()
end_time = time.time()
print("elapsed time : ", end_time-start_time)
