'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''
def check_row(sudoku, row):
    nineGrouping = []
    for cell in grid[row]:
        nineGrouping.append(cell)
    return check_no_dups(nineGrouping)

def check_column(sudoku, column):
    nineGrouping = []
    for row in grid:
        nineGrouping.append(row[column])
    return check_no_dups(nineGrouping) 

def check_subgrid(sudoku, row, column):
    nineGrouping = []
    for i in range(row, row + 3):
        for j in range(column, column + 3):
            nineGrouping.append(grid[i][j])
    return check_no_dups(nineGrouping)


def check_no_dups(nineGrouping):  
    uniqueDigits = set()
    for num in nineGrouping:
      if num != 0:
        if num  in uniqueDigits:
          return False
      uniqueDigits.add(num)
    return True

def all_digits(sudoku):
    for row in sudoku:
        for cell in row:
            try:
                int_value = int(cell)
                if int_value < 0 or int_value > 9 or int_value != cell:
                    return False
            except:
                return False
    return True   
def nine_by_nine(sudoku):
    if not sudoku:
        return False
    if len(sudoku) != 9:
        return False
    for row in sudoku:
        if len(row) != 9:
            return False
    return True   

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    if not nine_by_nine(sudoku) or not all_digits(sudoku):
      return None
    for i in range(0, 9):
        if not check_row(sudoku, i):
          return False
        if not check_column(sudoku, i):
            return False
    for i in range(0, 7, 3):
      for j in range(0, 7, 3):
        if not check_subgrid(sudoku, i, j):
          return False

    return True



def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()