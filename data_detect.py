from htmldate import find_date
from datetime import date
import requests

def TransformData(data):
    return str(data)[:4] + str(data)[5:7] + str(data)[8:11]
    
def DiferentaData(data1, data2):
    y1 = int(data1[:4])
    y2 = int(data2[:4])
    m1 = int(data1[4:6])
    m2 = int(data2[4:6])
    z1 = int(data1[6:8])
    z2 = int(data2[6:8])
    d1 = z1 + m1*30 + (y1-1900)*365
    d2 = z2 + m2*30 + (y2-1900)*365
    diff = d1 - d2
    return diff
    
def TitluArticol(url):
    hearders = {'headers':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0'}
    n = requests.get(url, headers=hearders)
    al = n.text
    return al[al.find('<title>') + 7 : al.find('</title>')]

url=str(input("introduceti adresa articolului, linkul= "))
titlu = TitluArticol(url)

data=TransformData(find_date(url))
print('Titlu articol:', titlu)
print('Data articol:', data)

today = TransformData(date.today())
print("Data de azi: ", today)

if data==today:
   print("este un articol scris astazi")
else:
   dif = DiferentaData(today, data)
   print('articolul este vechi de: ', dif, 'zile')
