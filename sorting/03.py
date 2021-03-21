n = int(input())
student_info = []

for _ in range(n):
    student_info.append(list(input().split()))

student_info.sort(key=lambda x: x[1])
for student in student_info:
    print(student[0], end=' ')
print()
