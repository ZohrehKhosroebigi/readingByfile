import nltk
import re
from hazm import *
import os
class Lemmiz():
    def lemmiz(self,doc1_name, doc2_name):
          # hazm test
            hazm_lemmatizer = Lemmatizer()
            print(hazm_lemmatizer.lemmatize('مادربزرگش'))
            lem_doc = []
            lem_query = []
            if not os.path.exists("logs"):
                os.mkdir("logs")
            doc1 = open(doc1_name, 'r', encoding='utf8')
            doc2 = open(doc2_name, 'r', encoding='utf8')
            for line in doc1:
                # print(line)
                words = re.findall(r'\w+', line)
                for word in words:
                    print("lemm of --------------",str(word))
                    lem_doc.append(hazm_lemmatizer.lemmatize(word))
            print("lemmitzaton doc---" + str(lem_doc))
            for line in doc2:
                words = re.findall(r'\w+', line)
                for word in words:
                    print("lemm of --------------",str(word))
                    lem_query.append(hazm_lemmatizer.lemmatize(word))
            print("lemmitzaton query---" + str(lem_query))
            self.name_lem_doc='logs/lemm_doc.txt'
            fhandw = open(self.name_lem_doc, 'w', encoding='utf8')
            b = " ".join(str(e) for e in lem_doc)
            fhandw.write(str(b))
            self.name_lem_query='logs/lemm_query.txt'
            fhandw = open(self.name_lem_query, 'w', encoding='utf8')
            b = " ".join(str(e) for e in lem_query)
            fhandw.write(str(b))
            return self.name_lem_doc,self.name_lem_query


