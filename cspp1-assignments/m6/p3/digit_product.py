'''GIVEN A NUMBER, FIND THE PRODUCT OF THE DIGITS'''
NUM = int(input())
COUNT = 0
PROD = 1
while NUM != 0:
    REM = NUM%10
    if REM == 0:
        print(0)
        COUNT = COUNT+1
        break
    else:
        PROD = PROD*REM
        NUM = NUM//10
if COUNT != 0 and REM == 0:
    print(0)
elif NUM == 0:
    print(0)
