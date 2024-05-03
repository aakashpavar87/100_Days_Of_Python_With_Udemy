row1 = ['🔥','🔥','🔥']
row2 = ['🔥','🔥','🔥']
row3 = ['🔥','🔥','🔥']
map = [row1,row2,row3]
location = input("Enter the location in Row and Column: ")
row_idx = int(location[0])
clo_idx = int(location[1])
# print(row_idx,clo_idx)
map[row_idx-1][clo_idx-1] = 'X'

print(f"{row1}\n{row2}\n{row3}")
# print(map)