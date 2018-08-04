'''GIVEN A NUMBER, FIND THE PRODUCT OF THE DIGITS'''
NUM = int(input())
COUNT = 0
PROD = 1
COUNT2 = 0
while NUM != 0 or NUM < 0:
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
