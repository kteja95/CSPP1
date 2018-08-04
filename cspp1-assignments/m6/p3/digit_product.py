'''GIVEN A NUMBER, FIND THE PRODUCT OF THE DIGITS'''
NUM = int(input())
if NUM == 0:
    print(0)
PROD = 1
while NUM > 0 and NUM != 0:
    REM = NUM%10
    PROD = PROD*REM
    NUM = NUM//10
print(PROD)
