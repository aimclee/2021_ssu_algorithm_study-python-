import time
start_time = time.time()

n=int(input())
student=[]
for i in range(n):
    inputs = input().split()
    student.append((inputs[0],int(inputs[1]))) # 튜플로 묶어준 다음에 리스트에 저장한다.

def score_func(data):
    return data[1]

student=sorted(student, key=score_func)

for j in range(len(student)):
    print(student[j][0],end=' ')


end_time = time.time()
print("time: ", end_time - start_time)