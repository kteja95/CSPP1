def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''

def main():
    # read matrix 1


    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    m1 = []
    m2 = []
    n = int(input())
    m = int(input())
    for j in range(n*m):
        m1.append(j)
        for i in range(0, m, 1):
            if i<=m:
                m2.append(m1)
            else:
                m2.append('\n')
    # print(m1)
    print(m2)


if __name__ == '__main__':
    main()
