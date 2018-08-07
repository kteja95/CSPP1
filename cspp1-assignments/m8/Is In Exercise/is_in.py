'''THE PROGRAM SEARCHES FOR A CHARACTER'''

def isIn(char, aStr):
    '''THE FUNCTION DOES THE SEARCH FOR CHARACTER'''
    i = 0
    if len(aStr)==0:
        return False
    else:
        if char != aStr[i]:
            return isIn(char,aStr[i+1:])
        else:
            return True


    
   

def main():
    data = input()
    data = data.split()
    print(isIn(data[0], data[1]))
   
if __name__== "__main__":
    main()