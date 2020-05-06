import logging
import numpy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
logging.basicConfig(level=logging.DEBUG,filename='logs/cosine.logs', filemode='w')
#doc_trump = "Mr. Trump became president after winning the political election. Though he lost the support of some republican friends, Trump is friends with President Putin"
#doc_election = "President Trump says Putin had no political interference is the election outcome. He says it was a witchhunt by political parties. He claimed President Putin is a friend who had nothing to do with the election"
#doc_putin = "Post elections, Vladimir Putin became President of Russia. President Putin had served as the Prime Minister earlier in his political career"
doc1 = open('logs/lemm_doc.txt', 'r', encoding='utf8')
doc2 = open('logs/lemm_query.txt', 'r', encoding='utf8')

for line in doc1:
    #dataset1=line
    dataset1 = 'a little bird'
for line in doc2:
    #dataset2=line
    dataset2 = 'a little bird chirps'

dataset = [dataset1,dataset2]

vectorizer = TfidfVectorizer()
X_tfidf = vectorizer.fit_transform(dataset)


# ...you say you are already at this point here...

sims = cosine_similarity(X_tfidf, X_tfidf)
rank = list(reversed(numpy.argsort(sims[0])))

#logging.debug("\nTdidf: \n%s" % X_tfidf.toarray())
logging.debug("\nSims: \n%s", sims)
#logging.debug("\nRank: \n%s", rank)