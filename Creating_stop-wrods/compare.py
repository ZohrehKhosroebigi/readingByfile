import  re
import nltk

f1 = open ('allkey.txt', 'r', encoding='utf8')
f2 = open ('allval.txt', 'r', encoding='utf8')
f3 = open ('stopwords_news.dict','r',encoding='utf8')

fhands1 = open('stopword_calcualtetxt', "w", encoding='utf8')
fhands2 = open('stopword_new__.txt', "w", encoding='utf8')
key=[]
val=[]
c=[]
for line in f1:
    words=line.split()
    for w in words:
        key.append(w)
for line in f2:
    words=line.split()
    for w in words:
        val.append(w)

for line in f3:
    words=line.split()
    for w in words:
        c.append(w)
mydic={}
for i in c:
    if i in key:
        #print(i)
        idx=key.index(i)
        #print(idx)
        mydic[i]=int(val[idx])
print(mydic)

for k, v in sorted(mydic.items(), key=lambda item: item[1], reverse=True):

     fhands1.write(str(k) + "-------"+str(v)+'\n')
     fhands2.write(str(k)+' ')




