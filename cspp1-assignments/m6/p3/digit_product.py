'''GIVEN A NUMBER, FIND THE PRODUCT OF THE DIGITS'''
NUM = int(input())
PROD = 1
while NUM > 0:
    REM = NUM%10
    PROD = PROD*REM
    NUM = NUM/10
print(PROD)
