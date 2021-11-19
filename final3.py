from newspaper import Article
import sys
import os
import re
import urllib.request

nume_fisier=1

fisier = sys.argv[1]
print(fisier)
with open(fisier, 'r') as fr:
    try:
        os.mkdir('stiri')
    except:
        pass
    os.chdir('stiri')
    for i in range (3):
        for i, line in enumerate(fr):
            with open('stire_'+str(i)+'.txt', 'wb') as fw:
                try:
                    result = 'Descarc: [' + line.strip() + '] ............ '
                    urlstire=line.strip()
                    article = Article(urlstire)
                    article.download()
                    article.parse()
                    fw.write(article.text.encode('utf-8'))
                    result = result + '[OK]'
                    #fw.write(article.publish_date)
                    #fw.write(article.authors)
                    #print(article.authors+' : '+article.publish_date)
                except:
                    result = result + '[EROARE]'
                
                print(result)
os.chdir('..')
