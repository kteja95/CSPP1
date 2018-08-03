#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

def main():
    string=input()
    c=0
    for i in range(0 , len(string) , 1):
        if(string[i]=='a' or string[i]=='e' or string[i]=='i' or string[i]=='o' or string[i]=='u'):
            c+=1
    print("No: of vowels in the string:" , c)


if __name__== "__main__":
    main()
