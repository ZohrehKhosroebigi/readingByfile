import nltk
import re
from hazm import *
import os
class Stemer_():
    def stem_(self,doc1_name, doc2_name):
          # hazm test
            hazm_stemmer = Stemmer()
            print(hazm_stemmer.stem('مادربزرگش'))
            stem_doc = []
            stem_query = []
            if not os.path.exists("logs"):
                os.mkdir("logs")
            doc1 = open(doc1_name, 'r', encoding='utf8')
            doc2 = open(doc2_name, 'r', encoding='utf8')
            for line in doc1:
                # print(line)
                words = re.findall(r'\w+', line)
                for word in words:
                    print("stem of --------------",str(word))
                    stem_doc.append(hazm_stemmer.stem(word))
            print("stem doc---" + str(stem_doc))
            for line in doc2:
                words = re.findall(r'\w+', line)
                for word in words:
                    print("stem of --------------",str(word))
                    stem_query.append(hazm_stemmer.stem(word))
            print("stem query---" + str(stem_query))
            self.name_stem_doc='logs/stem_no_doc.txt'
            fhandw = open(self.name_stem_doc, 'w', encoding='utf8')
            b = " ".join(str(e) for e in stem_doc)
            fhandw.write(str(b))
            self.name_stem_query='logs/stem_no_query.txt'
            fhandw = open(self.name_stem_query, 'w', encoding='utf8')
            b = " ".join(str(e) for e in stem_query)
            fhandw.write(str(b))
            return self.name_stem_doc,self.name_stem_query


