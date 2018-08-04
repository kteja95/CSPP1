''' REPLACING ALL SPECIAL CHARACTERS'''
STR1 = input()
STR2 = " "
for i in STR1:
    if i in "!@#$%^&*":
        STR1 = "  "
    else:
        STR2 += i
print(STR1, end=" ")
