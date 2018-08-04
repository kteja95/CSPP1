''' PROGRAM TO PRINT THE NUMBERS FROM 1 TO N'''
n=int(input())
for i in range(1, n+1, 1):
	if(i%3==0):
		print("Fizz",end="")
	elif(i%5==0):
		print("Buzz",end="")
	elif(i%3==0 and i%5==0):
		print("Fizz\nBuzz", end="")
	else:
		print(i,end="")