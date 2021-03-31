# 내 풀이
s=input()

result=1

# s에 들어온 문자열을 모두 int형 리스트로 반환
num=[]
for i in range(len(s)):
    num.append(int(s[i]))

# 내림차순 정렬
num.sort(reverse=True)

# 모든 숫자가 0일 경우 예외처리
if num.count(0)==len(s):
    print(0)

else:
    for i in num:
        if i == 0:
            continue
        result*=i
    print(result)


# 책의 풀이 -> 근데 이게 왜 그리디임??
'''
data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result+=num
    else:
        result*=num
print(result)
'''