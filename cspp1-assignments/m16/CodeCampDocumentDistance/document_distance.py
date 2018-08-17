'''
    Document Distance - A detailed description is given in the PDF
'''
import math, re
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    stop=load_stopwords("stopwords.txt")
    # final_list = []
    temp = 0
    # mult = 1
    sums = 0
    f=0
    words1 = []
    words2 = []
    str1 = dict1.lower()
    str2 = dict2.lower()
    # t = ["" "'a'!@#$%^&*()"]
    new1 = re.sub(r'[^a-z ]', '', str1).strip().split()
    new2 = re.sub(r'[^a-z ]', '', str2).strip().split()
    common_dict = {}
    # d1 = {}
    # d2 = {}
    for characters in new1:
        if characters not in stop:
            words1.append(characters)
    for lines in new2:
        if lines not in stop:
            words2.append(lines)
    for name in words1:
        if name in common_dict:
            common_dict[name][0]+=1
        else:
            common_dict[name]=[1, 0]
    for items in words2:
        if items in common_dict:
            common_dict[items][1]+=1
        else:
            common_dict[items] = [0, 1]
    # print(common_dict)
    for keys in common_dict:
        sums =sums+(common_dict[keys][0]*common_dict[keys][1])
    numerator = sums
    for keys in common_dict:
        temp=temp+(common_dict[keys][0]**2)
    for keys in common_dict:
        f = f+(common_dict[keys][1]**2)
    denominator = math.sqrt(temp)*math.sqrt(f)
    return (numerator/denominator)

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
