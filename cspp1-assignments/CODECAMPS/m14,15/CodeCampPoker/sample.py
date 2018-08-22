a= [2, D, 3, S, 5, S, 4, C, 6, D]
r = a.replace(" ","")
r = list(r[::2])
print(sorted(r))
# a=list(a).join(" ")
# print(a.strip())