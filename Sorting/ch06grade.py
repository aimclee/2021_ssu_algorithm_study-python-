tc = int(input())
dic = {}
for i in range(tc):
    input_data = input().split()
    #이름기준 성적 dictionary
    dic[input_data[0]] = (int(input_data[1]))
#print(dic)
dic = sorted(dic.items() , key = lambda x : x[1])

for data in dic:
    print(data[0], end=' ')