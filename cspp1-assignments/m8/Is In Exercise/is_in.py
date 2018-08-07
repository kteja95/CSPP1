# Exercise: Is In
# Write a Python function, isIn(char, aStr), that takes in two arguments a character and String and retuns the isIn(char, aStr) which retuns a boolean value.

# This function takes in two arguments character and String and returns one boolean value.

def isIn(char, aStr):
    print(char,aStr)
    if aStr==None:
        return False
    if len(aStr) == 1:
        return aStr == char

    middle = len(aStr)//2
    midChar = aStr[middle]

    if char == midChar:
        return True
    elif char < midChar:
        return isIn(char, aStr[:middle])
    else:
        return isIn(char, aStr[middle:])


def main():
    data = input()
    data = data.split()
    print(isIn(data[0], data[1]))
   
if __name__== "__main__":
    main()