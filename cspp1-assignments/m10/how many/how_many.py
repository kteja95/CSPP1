''' RETURN THE SUM OF VALUES IN A DICTIONARY'''
def how_many(aDict):
    sum = 0
    for k in aDict:
        sum = sum + len(aDict[k])
    print(sum)
  
    
    

def main():
    n=input()
    animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
    animals['d'] = ['donkey']
    animals['d'].append('dog')
    animals['d'].append('dingo')
    for i in range(int(n)):
        s=input()
        l=s.split()
        if l[0][0] not in animals:
            animals[l[0][0]]=[l[1]]
        else:
            animals[l[0][0]].append(l[1])
    print(how_many(animals))


if __name__== "__main__":
    main()