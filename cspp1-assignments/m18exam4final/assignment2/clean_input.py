'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
    ''' THIS FUNCTION USES REGEX TO MATCH ANY CHARACTER WITH THE CONDITION SPECIFIED'''

    text = re.sub(r'[^a-zA-Z0-9]', '', string)
    return text


def main():
    ''' THE MAIN IS USED TO TAKE INPUT AND CALL THE FUNCTION'''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
