import sys
# p196, 부록 참조
# 하나의 문자열 데이터 입력받기
# 주로 이진탐색 + 처리 데이터 1000만단위 이상일 경우
input_data = sys.stdin.readline().rstrip()

input_int_data_1, input_int_data_2 = map(int, sys.stdin.readline().split())

# 입력받은 문자열 그대로 출력하기
print(input_data)
print(input_int_data_1, input_int_data_2)