#Exercise : Biggest Exercise
#Write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values associated with it. If there is more than one such entry, return any one of the matching keys.


def biggest(aDict):
    biggestkey=[]
    flag=0
    for i in aDict.keys():
        length = len(aDict[i])
        if length >= flag:
            flag = length
            biggestkey=i
    return biggestkey

    




   


def main():
    n=input()
    aDict={}
    for i in range(int(n)):
        s=input()
        l=s.split()
        if l[0][0] not in aDict:
            aDict[l[0][0]]=[l[1]]
        else:
            aDict[l[0][0]].append(l[1])
    print(aDict) 
    print(biggest(aDict))
    


if __name__== "__main__":
    main()