#Exercise : Odd Tuples
#Write a python function oddTuples(aTup) that takes a some numbers in the tuple as input and returns a tuple in which contains odd index values in the input tuple  



def oddTuples(aTup):
    newTup = ()
    temp=0
    count=0
    for i in range(len(aTup)):
        if i%2==0:
            count = count+1
        else:
            newTup+= aTup[i],
    return newTup

  
    

def main():
    data = input()
    data = data.split()
    aTup=()
    for j in range(len(data)):
        aTup += ((data[j]),)
    print(oddTuples(aTup))
        

if __name__ == "__main__":
    main()