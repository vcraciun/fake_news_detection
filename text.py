import os

import unicodedata


def remove_accents(text):
    """
    Strip accents from input String.

    :param text: The input string.
    :type text: String.

    :returns: The processed String.
    :rtype: String.
    """
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)

def remove_accents2(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

folder= input("Ce folder analizati : ")
files=os.listdir(folder)
# creating an empty list
lst = []

# number of elemetns as data_ro
n = int(input("Introduceti cate cuvinte cheie doriti sa cautati : "))
keys=[]
# iterating till the range
for i in range(0, n):
    koi = str(input())

    keys.append(remove_accents(koi))  # adding the element

for file in files:
    if '.txt' in file:
        
        f = open(folder+os.sep+file, encoding='utf-8')# encoding='iso-8859-2')
        data = f.read()
        data = remove_accents(data)

        f.close()
        visited = []
        for key in keys:
            if (key) in str(data) and key not in visited:
               visited += [key]               
               
        if len(visited)==len(keys):
            path = os.path.join(folder, 'result.txt')
            f2 = open(path, 'a', encoding='ISO-8859-2')


            f2.write(data)
            f2.write('\r')


            f2.close()
            flag=False

