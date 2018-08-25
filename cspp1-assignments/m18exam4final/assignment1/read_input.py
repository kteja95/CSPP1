'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    ''' THE MAIN HERE TAKES MULTIPLE LINES INTO A STRING AND PRINTS IT'''
    t_1 = ''
    l_1 = int(input())
    for _ in range(l_1):
        t_1 = "".join(input())
        print(t_1)



if __name__ == '__main__':
    main()
