# 최악의 경우 시간복잡도 : O(n), n : 데이터의 개수

def sequential_search(size, array, target):
    for i in range(size):
        if array[i] == target:
            return i+1

        
print("입력할 원소의 개수와 찾을 문자열을 띄어쓰기로 구분하여 입력")
input_data = input().split()
num = int(input_data[0])
target = input_data[1]

print("위에서 입력한 개수만큼 삽입할 문자열 입력")
array = list(input().split())

print(sequential_search(num, array, target), "번째에 위치")
