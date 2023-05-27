
example=[
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0], 
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0, 0],
]
#answer 11

map_list=example

map_rows= len(example)
map_cols= len(example[0])
print("The maps is",map_rows,"Rows", "by", map_cols,"cols")

#stop top left check down if 1 move right 
#keep how many moves per line 
#re write the line with the most moves to 0s to delete
#?? flaws

print(map_list)

start_row=0
start_col=0

current_row=0
current_col=0

#for i in range(map_cols):
    