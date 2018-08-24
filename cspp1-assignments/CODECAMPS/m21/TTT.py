def tictactoe(matrix1):
    matlen1 = [3, 3]
    k = matlen1[0]-1
    elecount = 0
    flag = 0
    distinct = 0
    unique = 0
    count = 0
    temp = 0
    new = []
    for i in range(0, len(matrix1), 1):
        for j in range(len(matrix[i])-1):
            if matrix1[i][j] == matrix1[i][j+1]:
                elecount+=1
                new = matrix1[i][j]
                if elecount == len(matrix1[i])-1:
                    break
        break
                else:
                        continue
            
            elif matrix1[i][j] == matrix1[i+1][j+1] == matrix1[i+2][j+2]:
                temp+=1
                new = matrix1[i][j]
                break
        break
            elif matrix1[i][k] == matrix1[i+1][k-1] == matrix1[i+2][k-2]:
                flag+=1
                new = matrix1[i][l]
                break
        break
            elif matrix1[i][j] == matrix1[i+1][j] == matrix1[i+2][j]:
                unique+=1
                new = matrix1[i][k]
                break
        break
            elif matrix1[i][j+1] == matrix1[i+1][j+1] == matrix1[i+2][j+1]:
                distinct+=1
                new = matrix1[i][j]
                break 
        break
            elif matrix[i][k] == matrix[i+1][k] == matrix[i+2][k]:
                count+=1
                new = matrix[i][k]
                break
        break
    if elecount >0:
        return set(new)
    elif temp >0:
        return set(new)
    elif flag >0:
        return set(new)
    elif unique >0:
        return set(new)
    elif distinct >0:
        return set(new)
    elif count >0:
        return set(new)

def read_matrix(matlen):
    rows = []
    for i in matlen[0]:
        row = input()
        row = list(map(int, row.split(' ')))
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
    print(tictactoe(matrix1))

if __name__ == '__main__':
    main()
