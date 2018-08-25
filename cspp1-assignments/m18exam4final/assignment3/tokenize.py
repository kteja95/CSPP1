'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re
def tokenize(string):
    dict1 = {}
    text = re.sub(r'[^a-zA-Z]', " ", string)
    words = text.split()
    for items in words:
        if items in dict1:
            dict1[items] += 1
        else:
            dict1[items] = 1
    return dict1

 
            
def main():
    string = '' 
    lines = int(input())
    for i in range(lines):
        text = ''.join(input())
        print(tokenize(text))




if __name__ == '__main__':
    main()
