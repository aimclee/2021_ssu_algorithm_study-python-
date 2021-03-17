import time
start_time = time.time()


n = int(input())
move_plan = list(map(str,input().split()))
move_list = ['L','R','U','D']
move = [-1,1,-1,1]
x,y=1,1

for i in range(n):
	if x<=0:
		x+=1
		continue
	if x>=n-1:
		x-=1
		continue
	if y<=0:
		y+=1
		continue
	if y>=n-1:
		y-=1
		continue
	if move_plan[i] == 'L':
		y+=move[0]
	elif move_plan[i] == 'R':
		y+=move[1]
	elif move_plan[i] == 'U':
		x+=move[2]
	elif move_plan[i] == 'D':
		x+=move[3]
		
print(x+1,y+1)

end_time = time.time()
print("time: ", end_time - start_time)
