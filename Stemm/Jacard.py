import nltk
import re
from hazm import *
import os
class JacardSimilarity():
    def jacardsimilarity(self,doc1_name, doc2_name):
            fhandw = open("logs/jaccard_stem.txt", 'w', encoding='utf8')
            #hazm test
            stem_doc=""
            stem_query=""
            doc1_name='logs/stem_doc.txt'
            doc2_name='logs/stem_query.txt'
            if not os.path.exists("logs"):
                os.mkdir("logs")
            doc1 = open(doc1_name, 'r', encoding='utf8')
            doc2 = open(doc2_name, 'r', encoding='utf8')
            for line in doc1:
                stem_doc = stem_doc + line
            for line in doc2:
                stem_query = stem_query + line

            lem_doc = stem_doc.split()
            lem_query = stem_query.split()

           #jacard
            intersection = set(lem_query).intersection(set(lem_doc))
            print("intersection is --------",str(intersection))
            union = set(lem_query).union(set(lem_doc))
            print("union is --------", str(union))
            self.jacard = len(intersection) / len(union)
            print("--jaccard is ---" + str(self.jacard))
            fhandw.write(str(self.jacard))
            return self.jacard