import copy
import math
    
def tictactoe(matrix1):
    matlen1 = [3, 3]
    k = matlen1[0]-1
    ocount = 0
    xcount =0
    flag = 0
    distinct = 0
    unique = 0
    count = 0
    temp = 0
    new = []
    for i in range(0, len(matrix1), 1):
        if matrix1[i].count('.') == 3:
            del matrix1[i]
            if matrix1[i+1].count('o')==3:
                new = copy.deepcopy(matrix1[i])
                ocount+=1
                    
            elif matrix1[i+1].count('x')==3:
                new = copy.deepcopy(matrix1[i+1])
                xcount+=1
                    
            if matrix1[i+1].count('o')==3 and matrix1[i+2].count('x')==3:
                return "invalid game"
            elif matrix1[i+1].count('x')==3 and matrix1[i+2].count('o')==3:
                return "invalid game"
        elif matrix1[i+1].count('.') == 3:
            del matrix1[i+1]
            if matrix1[i+2].count('o') == 3:
                new = copy.deepcopy(matrix1[i+2])
                ocount+=1
                    
            elif matrix1[i+2].count('x')==3:
                new = copy.deepcopy(matrix1[i+2])
                xcount+=1
            if matrix1[i].count('o') == 3 and matrix1[i+2].count('x') == 3:
                return "invalid game"
            elif matrix1[i].count('x') == 3 and matrix1[i+2].count('o') == 3:
                return "invalid game"


        elif matrix1[i+2].count('.') == 3:
            del matrix1[i+2]
            if matrix1[i].count('o')==3:
                new = copy.deepcopy(matrix1[i])
                ocount+=1
                    
            elif matrix1[i].count('x')==3:
                new = copy.deepcopy(matrix1[i+1])
                xcount+=1
                    
            if matrix1[i].count('o')==3 and matrix1[i+1].count('x')==3:
                return "invalid game"
            elif matrix1[i].count('x')==3 and matrix1[i+1].count('o')==3:
                return "invalid game" 
        if matrix1[i].count('o')==3 or matrix1[i+1].count('o')==3 or matrix1[i+2].count('o')==3:
            ocount+=1
            return 'o'
        elif matrix1[i].count('x')==3 or matrix1[i+1].count('x')==3 or matrix1[i+2].count('x')==3:
            xcount+=1
            return 'x'
        for j in range(len(matrix1[i])-1):

            if matrix1[i][j] == matrix1[i+1][j+1] and matrix1[i][j] == matrix1[i+2][j+2]:
                temp+=1
                new.append(matrix1[i][j])
                break

            elif matrix1[i][k] == matrix1[i+1][k-1] and matrix1[i][k] == matrix1[i+2][k-2]:
                flag+=1
                new.append(matrix1[i][k])
                break

            elif matrix1[i][j] == matrix1[i+1][j] and matrix1[i][j] == matrix1[i+2][j]:
                unique+=1
                new.append(matrix1[i][j])
                break

            elif matrix1[i][j+1] == matrix1[i+1][j+1] and matrix1[i][j+1] == matrix1[i+2][j+1]:
                distinct+=1
            elif matrix1[i][k] == matrix1[i+1][k-1] and matrix1[i][k] == matrix1[i+2][k-2]:
                count+=1
                new.append(matrix1[i][k])
                break
        break
    if ocount >0:
        if 'o' in set(new):
            return 'o'
    if xcount>0:
        if 'x' in set(new):
            return 'x'
    elif temp >0:
        if 'o' in set(new):
            return 'o'
        else:
            return 'x'
    elif flag >0:
        if 'o' in set(new):
            return 'o'
        else:
            return 'x'
    elif unique >0:
        if 'o' in set(new):
            return 'o'
        else:
            return 'x'
    elif distinct >0:
        if 'o' in set(new):
            return 'o'
        else:
            return 'x'
    elif count >0:
        if 'o' in set(new):
            return 'o'
        else:
            return 'x'
        
def read_matrix(matlen):
    rows = []
    for i in range(matlen[0]):
        row = input()
        row = list(map(str, row.split(' ')))
        rows.append(row)
    if matlen[0]!=len(rows):
        return None
    for i in rows:
        if len(i)!=matlen[1]:
            return None
    return rows


def main():
    matlen1 = [3, 3]
    matrix1 = read_matrix(matlen1)
    # if matrix1.count('x')-matrix1.count('o') > abs(1) or matrix1.count('x') == 9 or matrix1.count('o')==9:
    #     print("invalid game")
    # else:
    #     for i in range(0, len(matrix1), 1):
    #         if matrix1[i].count('x') == 2 or matrix1.count('o') == 2:
    #             continue
    #     print("draw")
    print(tictactoe(matrix1))

if __name__ == '__main__':
    main()
