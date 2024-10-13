# model.py

def create_board():
    return [[0, 0, 0], [0, 0, 0], [0, 0, 0]]



def check_winner(b):
    if b[0][0]>0 and b[0][0]==b[0][1] and b[0][1]==b[0][2]:
        return b[0][0]
    if b[1][0]>0 and b[1][0]==b[1][1] and b[1][1]==b[1][2]:
        return b[1][0]
    if b[2][0]>0 and b[2][0]==b[2][1] and b[2][1]==b[2][2]:
        return b[2][0]
    if b[0][0]>0 and b[0][0]==b[1][0] and b[1][0]==b[2][0]:
        return b[0][0]
    if b[0][1]>0 and b[0][1]==b[1][1] and b[1][1]==b[2][1]:
        return b[0][1]
    if b[0][2]>0 and b[0][2]==b[1][2] and b[1][2]==b[2][2]:
        return b[0][2]
    if b[0][0]>0 and b[0][0]==b[1][1] and b[1][1]==b[2][2]:
        return b[0][0]
    if b[2][0]>0 and b[2][0]==b[1][1] and b[1][1]==b[0][2]:
        return b[2][0]
    p=0
    for i in range(3):
        for j in range(3):
            p += (1 if b[i][j]>0 else 0)
    if p==9:
        return 3
    else:
        return 0

