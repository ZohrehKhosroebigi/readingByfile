"""temp2 = ['One', 'Two', 'Three', 'Four']
temp1 = ['One', 'Two']
print(list(set(temp1) - set(temp2)))"""

from sklearn.feature_extraction.text import TfidfVectorizer




import logging
import numpy
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
class CosineSimilarity():
    def cosinesimilarity(self,doc1,doc2):

        logging.basicConfig(level=logging.DEBUG, filename='logs/cosine_lemlogs', filemode='w')
        doc1 = open(doc1, 'r', encoding='utf8')
        doc2 = open(doc2, 'r', encoding='utf8')
        #doc1 = open('logs/lemm_doc.txt', 'r', encoding='utf8')
        #doc2 = open('logs/lemm_query.txt', 'r', encoding='utf8')
        dataset1=""
        dataset2=""
        for line in doc1:
            dataset1=dataset1+line
            #dataset1 = 'خدا'
        for line in doc2:
            dataset2=dataset2+line
            #dataset2 = 'خدا حافظ'
        dataset = [dataset1,dataset2]


        documents =  [dataset1,dataset2]
        tfidf = TfidfVectorizer().fit_transform(documents)
        # no need to normalize, since Vectorizer will return normalized tf-idf
        pairwise_similarity = tfidf * tfidf.T
        print("--cosine is -----"+str(pairwise_similarity))