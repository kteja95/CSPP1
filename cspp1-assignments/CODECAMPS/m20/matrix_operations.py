import copy
def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if len(m)!= len(m2[0]):
        print("Error : Matrix shapes invalid for mult")
        return None
    list1 = []
    for i in range(0, len(m), 1):
        list2 = []
        for j in range(0, len(m2[0]), 1):
            result = 0
            for k in range(0, len(m2), 1):
                result += int(m[i][k])*int(m2[k][j])
            list2.append(result)
        list1.append(list2)
    return list1


def add_matrix(m, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    l1 = len(m)
    l2 = len(m2)
    if l1!=l2:
        print("Error: Matrix shapes invalid for addition")
        return None
    else:
        result = copy.deepcopy(m)
        for i in range(0, l2, 1):
            for j in range(0, len(m2[i]), 1):
                result[i][j] = int(result[i][j])
                result[i][j] += int(m2[i][j])
        return result



def read_matrix(size):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    r = int(size[0])
    c = int(size[1])
    t = 0
    m = []
    for i in range(0, r, 1):
        r = input().split()
        m.append(r)
        t+=len(r)
    if t!=r*c:
        print("Error: Invalid input for the matrix")
    else:
        return m

def main():
    num1 = input().split(',')
    m = read_matrix(num1)
    num2 = input().split(',')
    
    # print(m)
    m2 = read_matrix(num2)
    # print(m2)
    if m == None or m2 == None:
        return None
    print(add_matrix(m, m2))
    print(mult_matrix(m, m2))




if __name__ == '__main__':
    main()
