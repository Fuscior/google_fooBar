import math
'''
possible knight moves 
        x[+2] y[+1]
        x[+2] y[-1] 
        x[-2] y[+1]
        x[-2] y[-1] 

        x[+1] y[+2]
        x[+1] y[-2]
        x[-1] y[+2]
        x[-1] y[-2]
'''
knight_moves= [
    [2,1],
    [2,-1],
    [-2,1],
    [-2,-1],
    [1,2],
    [1,-2],
    [-1,2],
    [-1,-2]
]
#board[8][8] 8*8=64 squares
chess_board= [
    [0,1,2,3,4,5,6,7],
    [8,9,10,11,12,13,14,15],
    [16,17,18,19,20,21,22,23],
    [24,25,26,27,28,29,30,31],
    [32,33,34,35,36,37,38,39],
    [40,41,42,43,44,45,46,47],
    [48,48,50,51,52,53,54,55],
    [56,57,58,59,60,61,62,63],
]

'''
valid move finsih 
            locate x> 0 && x< 8
            locate y> 0 && y<8
'''

src=0
des=0

def Solution(src, des):
    #work in prog
    start_locate=src
    destination=des
    isFound=False
    move_count=0
    current_pos_list=[start_locate]
    
    if start_locate == destination:
        return move_count

    while isFound == False:
        for j in range(len(current_pos_list)):
            #print("the lenght of the array is ", len(current_pos_list))
            x_locate= int(current_pos_list[j] / 8)
            y_locate= current_pos_list[j] % 8

            #print("The location is [", x_locate, "]", "[", y_locate, "]")
            #print("The square number is: ",chess_board[x_locate][y_locate])
            ##generate moves 8 possible
            for i in range(8):
                x_move= x_locate + knight_moves[i][0]
                y_move= y_locate + knight_moves[i][1]
                if x_move >=0 and x_move <=7 and y_move >= 0 and y_move <=7:
                    current_pos_list.append(chess_board[x_move][y_move])
            for x in range(len(current_pos_list)):
                if current_pos_list[x] == destination:
                    isFound=True
        move_count= move_count +1


        
    #print(current_pos_list)
    #print(move_count)
    return move_count

print(Solution(src, des))


    
        

