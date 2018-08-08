'''THIS PROGRAM REPLACES UNMATCHED CHARS WITH _'''
def get_guessed_word(secret_word, letters_guessed):
    str1=''
    for i in range(0, len(secret_word), 1):
        if secret_word[i] in letters_guessed:
            str1+=secret_word[i]
        else:
            str1+='_'
    return str1   
    
    

def main():
    '''
    Main function for current assignment
    '''
    user_input = input()
    if user_input:
        data = user_input.split()
        secret_word = data[0]
    else:
        data = []
        secret_word = ""
    list1 = []
    for j in range(1, len(data)):
        list1.append(data[j])
    print(get_guessed_word(secret_word, list1))

if __name__ == "__main__":
    main()
