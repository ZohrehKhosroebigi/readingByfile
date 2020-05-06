import operator

import re

fhankey = open('logs/1.txt', 'r', encoding='utf8')
fhandval = open('logs/2.txt', 'r', encoding='utf8')

mydic={}

key=[]
val=[]

for line in fhankey:
    key.append(line.split('\n'))
for line in fhandval:
    val.append(line.split('\n'))

for k, v in zip(key,val):
    if k!='\n' and v!='\n' and k not in mydic:
        mydic[k]=v
    else:
        mydic[k]+=v


fhandk = open('logs/all-key.txt', 'w', encoding='utf8')
fhandv = open('logs/all-val.txt', 'w', encoding='utf8')
for k, v in sorted(mydic.items(), key=lambda item: item[1], reverse=True):


        fhandk.write(str(k))
        fhandv.write ( str ( v )  )
