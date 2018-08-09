import string
def get_available_letters(letters_guessed):
    r=[]
    str1 = string.ascii_lowercase
    for i in str1:
        if i not in letters_guessed:
            r.append(i)
        else:
            continue
    return "".join(r)

    
            

    
def main():
    user_input = input()
    user_input = user_input.split()
    data = []
    for char in user_input:
        data.append(char[0])
    print(get_available_letters(data))


if __name__ == "__main__":
    main()
