'''GIVEN A NUMBER, FIND THE PRODUCT OF THE DIGITS'''
NUM = int(input())
PROD = 1
ZERONUM = 0
ZEROREM = 0
NONZEROREM = 0
while NUM != 0:
    REM = NUM%10
    if REM == 0:
        ZEROREM = ZEROREM+1
        break
    else:
        PROD = PROD*REM
        NUM = NUM//10
        NONZEROREM = NONZEROREM+1
if ZERONUM == 0:
    print(0)
elif ZEROREM > 0:
    print(0)
else:
    print(PROD)
    