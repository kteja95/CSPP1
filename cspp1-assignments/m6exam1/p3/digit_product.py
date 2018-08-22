'''GIVEN A NUMBER, FIND THE PRODUCT OF THE DIGITS'''
NUM = int(input())
COUNT = 0
PROD = 1
COUNT2 = 0
if NUM == 1:
    print(1)
if NUM == 2:
    print(2)
if NUM == 3:
    print(3)
if NUM == 4:
    print(4)
if NUM == 5:
    print(5)
if NUM == 6:
    print(6)
if NUM == 7:
    print(7)
if NUM == 8:
    print(8)
if NUM == 9:
    print(9)
else:
    while NUM != 0 and NUM > 9 or NUM < 0:
        REM = NUM%10
        if REM == 0:
            COUNT = COUNT+1
            break
        else:
            PROD = PROD*REM
            NUM = NUM//10
            COUNT2 = COUNT2 + 1
if NUM == 0:
    print(0)
if COUNT > 0:
    print(0)
elif COUNT2 > 0:
    print(PROD)
