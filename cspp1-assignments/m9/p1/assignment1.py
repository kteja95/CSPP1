'''THE PROGRAM CHECKS EVERY CHARACTER IN THE STRING'''


def is_word_guessed(secret_word, letters_guessed):
    ''' THIS FUNCTION CHECHKS FOR EVERY CHARACTER IN THE SECRET WORD'''
    t=0
    for i in range(0, len(secret_word), 1):
        if secret_word[i] in letters_guessed:
            t=t+1
        else:
            continue
    if t == len(secret_word):
        return True
    else:
        return False


def main():
    '''
    Main function for the program
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
    print(is_word_guessed(secret_word, list1))

if __name__ == "__main__":
    main()
