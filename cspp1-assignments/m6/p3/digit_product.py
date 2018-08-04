'''GIVEN A NUMBER, FIND THE PRODUCT OF THE DIGITS'''
NUM = int(input())
if NUM == 0:
    print(0)
else:
    PROD = 1
    while NUM != 0:
        REM = NUM%10
        if REM == 0:
            print(0)
            break
        else:
            PROD = PROD*REM
            NUM = NUM//10
print(PROD)
