arr=[]
rows, cols=5,5
for i in range(rows):
	col = []
	for j in range(cols):
		col.append(j+i)
	arr.append(col)
print(arr)


print(arr[0])


for i in range(rows):
    print(arr[i][0])
