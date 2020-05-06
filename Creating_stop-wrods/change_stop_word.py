import  re
import nltk

f3 = open ('stopwords_news.dict','r',encoding='utf8')

fhands4 = open('stopwords_news.dict_NEW.txt', "w", encoding='utf8')
mydic= {}

for line in f3:
    words=line.split()
    for w in words:
        mydic[w]=1
print(mydic)
for k, v in sorted(mydic.items(), key=lambda item: item[1], reverse=True):
    fhands4.write(str(k)+" ")

