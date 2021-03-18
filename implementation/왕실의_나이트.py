import time
start_time = time.time()

input_loc = input() #'a1'
move_list = [[-2,-1],[-2,1],[-1,2],[-1,-2],[2,1],[2,-1],[1,-2],[1,2]]
loc = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}

def column_num():
    for key, value in loc.items():
        if input_loc[0] == key:
            return value
column_num = column_num()

def move(column, row):
    answer=0
    for i in range(len(move_list)):
        j,k=move_list[i]
        column+=j
        row+=k
        if column<=0 or column>=9 or row<=0 or row>=9:
            column-=j
            row-=k
        else:
            answer+=1
            column-=j
            row-=k
    print(answer)

move(column_num, int(input_loc[1]))

end_time = time.time()
print("time: ", end_time - start_time)