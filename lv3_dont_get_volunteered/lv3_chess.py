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

print(chess_board[1][0])

'''
valid move finsih 
            locate x> 0 && x< 8
            locate y> 0 && y<8
'''


#work in prog

start_locate=56

x_locate= int(start_locate / 8)
y_locate= start_locate % 8

print("The location is [", x_locate, "]", "[", y_locate, "]")
print("The square number is: ",chess_board[x_locate][y_locate])