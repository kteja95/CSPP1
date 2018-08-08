#Exercise : Function and Objects Exercise-3
#Implement a function that converts the given testList = [1, -4, 8, -9] into [1, 16, 64, 81]

def square(L):
    # f=f**2
    return L**2

def apply_to_each(L):
    print(list(map(square, L)))





    
def main():
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    apply_to_each(list1)

if __name__== "__main__":
    main()