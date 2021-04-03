# 동빈북 p313
# 너무 복잡하게 풀려고 하지 말자
# 문제풀이 아이디어 자체는 맞음. 
# 숫자가 바뀌는 포인트에 집중하자

s=input()

zero_cnt=0
one_cnt=0

# temp_zero=0
# temp_one=0

if s[0] == '1':
    zero_cnt += 1
else:
    one_cnt +=1

# 범위 설정하는거 항상 시도해보려고 노력하자.
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '0':
            one_cnt+=1
        else:
            zero_cnt +=1

print(min(one_cnt, zero_cnt))


# temp = s_list[0]
# for i in range(1, len(s_list)):
#     # if temp == s_list[i] == '0':
#     temp_zero = temp + int(s_list[i])

#     if temp_one+1 > temp_zero :  
#         one_cnt+=1

#     if temp_zero == 1:
#         zero_cnt += 1
#         temp_zero = 0

#     elif temp_zero >= 2:
#         temp_one = temp + int(s_list[i])
#         temp = temp_one
#         continue
#         # one_cnt+=1

#         temp_zero = 0
#     temp = int(s_list[i])

