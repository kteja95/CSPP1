'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re
def tokenize(string):
    '''THIS FUNCTION RETURNS THE DICTIONARY'''
    dict1 = {}
    text = re.sub(r'[^a-zA-Z0-9]', " ", string)
    words = text.split()
    for items in words:
        if items in dict1:
            dict1[items] += 1
        else:
            dict1[items] = 1
    return dict1

def main():
    '''THE MAIN FUNCTION HERE PASSES THE STRING TO THE FUCNTION'''
    lines = int(input())
    for _ in range(lines):
        text = ''.join(input())
        print(tokenize(text))




if __name__ == '__main__':
    main()
