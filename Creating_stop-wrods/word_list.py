import  re
f1 = open ('D:/Persoanl data/FINAL_TEXT/FinalTxt1_WithoutSpaceNorm_NormAlpha.txt','r',encoding='utf8')
f2 = open ('D:/Persoanl data/FINAL_TEXT/FinalTxt2_WithoutSpaceNorm_NormAlpha.txt','r',encoding='utf8')
f3 = open ('D:/Persoanl data/FINAL_TEXT/FinalTxt3_WithoutSpaceNorm_NormAlpha.txt','r',encoding='utf8')
f4 = open ('D:/Persoanl data/FINAL_TEXT/FinalTxt4_WithoutSpaceNorm_NormAlpha.txt','r',encoding='utf8')
f5 = open ('D:/Persoanl data/FINAL_TEXT/FinalTxt5_WithoutSpaceNorm_NormAlpha.txt','r',encoding='utf8')
fhandkey = open('allkey.txt', "w", encoding='utf8')
fhandval = open('allval.txt', "w", encoding='utf8')

dic = dict ()
for line in f1:
    words=line.split()
    for word in  words:
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] += 1
f1.close()

for line in f2:
    words=line.split()
    for word in  words:
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] += 1
f2.close()

for line in f3:
    words=line.split()
    for word in  words:
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] += 1
f3.close()


for line in f4:
    words=line.split()
    for word in  words:
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] += 1
f4.close()


for line in f5:
    words=line.split()
    for word in  words:
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] += 1
f5.close()

for k, v in sorted(dic.items(), key=lambda item: item[1], reverse=True):

    if v >30:
        fhandkey.write(str(k) +'\n')
        fhandval.write ( str ( v ) + '\n' )




