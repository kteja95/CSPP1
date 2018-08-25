'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    text = ''
    lines = int(input())
    for i in range(lines):
        text = "".join(input())
        print(text)



if __name__ == '__main__':
    main()
