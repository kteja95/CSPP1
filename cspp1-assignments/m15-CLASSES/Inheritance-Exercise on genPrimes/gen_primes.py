#define the gen_primes function here
def genPrimes():
     n = 2
     primes = set()
     while True:
         for p in primes:
             if n % p == 0:
                 break
            else:
                primes.add(n)
                yield n
        n += 1
    

def main():
    data=input()
    l=data.split()
    a=int(l[0])
    b=int(l[1])
    primeGenerator = genPrimes()
    for i in range(a):
        p=primeGenerator.next()
        if(i%b==0):
            print p
    
if __name__== "__main__":
    main()
