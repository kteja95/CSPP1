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
        for j in range(len(matrix1[i])-1):
            if matrix1[i][j] == matrix1[i][j+1]:
                elecount+=1
                new.append(matrix1[i][j])
                if elecount == len(matrix1[i])-1:
                    break

            elif matrix1[i][j] == matrix1[i+1][j+1] == matrix1[i+2][j+2]:
                temp+=1
                new.append(matrix1[i][j])
                break

            elif matrix1[i][k] == matrix1[i+1][k-1] == matrix1[i+2][k-2]:
                flag+=1
                new.append(matrix1[i][k])
                break

            elif matrix1[i][j] == matrix1[i+1][j] == matrix1[i+2][j]:
                unique+=1
                new.append(matrix1[i][j])
                break

            elif matrix1[i][j+1] == matrix1[i+1][j+1] == matrix1[i+2][j+1]:
                distinct+=1
            elif matrix1[i][k] == matrix1[i+1][k-1] == matrix1[i+2][k-2]:
                count+=1
                new.append(matrix1[i][k])
                break
        break
    if elecount >0:
        if 'o' in set(new):
            return 'o'
        else:
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
    print(tictactoe(matrix1))

if __name__ == '__main__':
    main()
