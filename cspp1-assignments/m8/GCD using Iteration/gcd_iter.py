# Exercise: GCDIter
# Write a Python function, gcdIter(a, b), that takes in two numbers and returns the GCD(a,b) of given a and b.

# This function takes in two numbers and returns one number.


def gcdIter(a, b):
    if a>b:
        smaller = b
    else:
         smaller = a
    for i in range(1, smaller+1):
        if((a % i == 0) and (b % i == 0)):
            hcf = i
            
    return hcf



def main():
    data = input()
    data = data.split()
    print(gcdIter(int(data[0]),int(data[1]))) 

if __name__== "__main__":
    main()