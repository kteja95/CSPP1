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
    # print(tictactoe(matrix1))

if __name__ == '__main__':
    main()
