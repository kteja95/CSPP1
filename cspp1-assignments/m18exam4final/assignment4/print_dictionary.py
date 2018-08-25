'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dictionary):
    '''THIS FUCNTION DOES THE KEYS SORTING'''
    for keys in sorted(dictionary):
        print(keys, "-", dictionary[keys])

def main():
    '''THIS FUCNTION CALLS THE ABOVE FUCNTION'''
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
