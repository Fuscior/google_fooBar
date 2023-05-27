
example=[
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0], 
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0, 0],
]
#answer 11

map_array=example

map_rows= len(example)
map_cols= len(example[0])
print("The maps is",map_rows,"Rows", "by", map_cols,"cols")

#look in next row for 0 if zero save col index 
#check vs current door 
#min result is new door
#biggest diff from prv door to new door = bigest wall to delete


start_row=0
start_col=0

current_row=start_row
current_col=start_col

door_way=0
possible_door_way=[]
possible_move_length=[]
total_moves=[]

for i in range(map_cols):
    if map_array[current_row+1][i] == 0:
        possible_door_way.append(i)
        print(possible_door_way)

    for x in range(len(possible_door_way)):
        possible_move_length.append(abs(door_way-possible_door_way[x]))
        possible_move_length.sort()
        print(possible_move_length)

        total_moves.append(possible_move_length[0])
