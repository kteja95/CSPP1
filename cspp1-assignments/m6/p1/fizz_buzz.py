''' PROGRAM TO PRINT THE NUMBERS FROM 1 TO N'''
NUM = int(input())
for i in range(1, NUM+1, 1):
    if i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    elif(i%3 == 0 and i% 5 == 0):
        print("Fizz")
        print("Buzz")
    else:
        print(i)
