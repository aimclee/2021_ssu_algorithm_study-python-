data = list(map(int, input()))

zero = 0  # 0덩어리 개수
one = 0   # 1덩어리 개수 

# 덩어리 끝에 도달해서 해당 덩어리가 1덩어리인지 0덩어리인지 판단하는 로직
for i in range(1, len(data)): 
    if data[i-1] != data[i]:
        if data[i-1] == 0:
            zero += 1
        else:
            one += 1
            
# 문자열 마지막 숫자
if data[i] == 0:
    zero += 1
else:
    one += 1
    
result = min(zero, one)
print(result)
