''' TO CALCULATE THE FACROIRAL'''


def factorial(n):
	'''TO CALCULATE THE FACT'''
	if n == 1:
		return 1
	return n*factorial(n-1)
    
    


def main():
    a = input()
    print(factorial(int(a)))  
    import sys
    sys.setrecursionlimit(25500)  

if __name__== "__main__":
    main()
