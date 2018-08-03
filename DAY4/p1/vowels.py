x=0
s=str(input("Enter a string of characters"))
for i in range(0 , len(s) , 1):
	if(s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u'):
		x+=1

print("No: of vowels in the string:" , x)
