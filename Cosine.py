import logging
import numpy
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
class CosineSimilarity():
    def cosinesimilarity(self,doc1,doc2):

        logging.basicConfig(level=logging.DEBUG,filename='logs/cosine.logs', filemode='w')
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

        # settings that you use for count vectorizer will go here
        tfidf_vectorizer = TfidfVectorizer(use_idf=True)
        tfidf_vectorizer_vectors = tfidf_vectorizer.fit_transform(dataset)

        # get the first vector out (for the first document)
        first_vector_tfidfvectorizer = tfidf_vectorizer_vectors[0]

        # place tf-idf values in a pandas data frame
        df = pd.DataFrame(first_vector_tfidfvectorizer.T.todense(), index=tfidf_vectorizer.get_feature_names(),
                          columns=["tfidf"])
        df.sort_values(by=["tfidf"], ascending=True)
        print("---TfidfVectorizer   tf-idf values--------",str(df))

        sims = cosine_similarity(tfidf_vectorizer_vectors,tfidf_vectorizer_vectors)
        rank = list(reversed(numpy.argsort(sims[0])))

        logging.debug("\nTdidf: \n%s" % tfidf_vectorizer_vectors.toarray())
        logging.debug("\nSims: \n%s", sims)
        logging.debug("\nRank: \n%s", rank)
##############################################################################
        print("******transfor******")
      ####Tfidftransformer Usage
        # instantiate CountVectorizer()
        count_vec=CountVectorizer()
        #print(dataset)
        # this steps generates word counts for the words in your docs  TF
        word_count_vector = count_vec.fit_transform(dataset)


        print("this is word_count_vector ---------",str( word_count_vector))

        #rows number of docs and columns are unique words, minus single character words
        print("this is word_count_vector.shape ---------",str(word_count_vector.shape))

        #Compute the IDF values
        tfidf_transformer = TfidfTransformer(smooth_idf=True, use_idf=True)
        tfidf_transformer.fit(word_count_vector)
        # print idf values
        df_idf = pd.DataFrame(tfidf_transformer.idf_, index=count_vec.get_feature_names(), columns=["idf_weights"])
        # sort ascending
        df_idf.sort_values(by=['idf_weights'])
        print("-------------------idf-")

        print((df_idf))
        # count matrix   Compute the TFIDF score for documents
        count_vector = count_vec.transform(dataset)
        # tf-idf scores
        tf_idf_vector = tfidf_transformer.transform(count_vector)

        ###print
        feature_names = count_vec.get_feature_names()
        # get tfidf vector for first document
        first_document_vector = tf_idf_vector[0]
        # print the scores
        df = pd.DataFrame(first_document_vector.T.todense(), index=feature_names, columns=["tfidf"])
        df.sort_values(by=["tfidf"], ascending=False)
        print(df)

        sims = cosine_similarity(tf_idf_vector, tf_idf_vector)
        rank = list(reversed(numpy.argsort(sims[0])))

        logging.debug("\nTdidf_transform:--------- \n%s" % tf_idf_vector.toarray())
        logging.debug("\nSims: \n%s", sims)
        logging.debug("\nRank: \n%s", rank)