from googlesearch import search
from htmldate import find_date
from datetime import date


import os
import requests
import shutil

date_time = ("documente")
os.makedirs(date_time, exist_ok=True)
print(f"o sa salvez in {date_time}")

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

query = (titlu)+("'site:gov'")
num = 7


log_file_path = f'{date_time}/logs.txt'
log_file = open(log_file_path, 'w')
results: list = search(query, num=int(num), start=0, stop=int(num), pause=5)
results_list = []
for url in results:
    log_file.write(f"{url}\n")
    results_list.append(url)
log_file.flush()
log_file.close()

cwd = os.path.curdir
cwd_log_file = os.path.join(cwd, 'logs.txt')
print(cwd_log_file)
shutil.rmtree(cwd_log_file, ignore_errors=True)
shutil.copy2(log_file_path, cwd_log_file)


def download_url(url_to_download, index, folder):
    print(url_to_download)
    local_filename = f'{index}_'+url_to_download.split('/')[-1]
    local_path = os.path.join(folder, local_filename)
    r = requests.get(url_to_download)
    f = open(local_path, 'wb')
    for chunk in r.iter_content(chunk_size=512 * 1024):
        if chunk:  # filter out keep-alive new chunks
            f.write(chunk)
    f.close()
    return


print("am terminat de cautat, acum incep descarcarea documentelor")
ix = 0
for url in results_list:
    try:
        download_url(url, ix, date_time)
    except Exception as ignored:
        pass
    ix += 1
