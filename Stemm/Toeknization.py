import os
import nltk
class Tokenization():

    def token(self,doc_name):
        if not os.path.exists("logs"):
            os.mkdir("logs")
        doc = open(doc_name, 'r', encoding='utf8')
        self.name=doc_name + 'token.txt'
        doc_stop_words=open('logs/stopword_new__.txt', 'r', encoding='utf8')
        stop_words=[]
        for line in doc_stop_words:
            stop_words = line.split()

        fhandw = open(self.name, 'w', encoding='utf8')
        fhanddiffstop = open('logs/diff.txt', 'w', encoding='utf8')
        tokenizer = nltk.RegexpTokenizer(r"\w+")
        for line in doc:
            token_query = tokenizer.tokenize(line)
            print(token_query)
            print(stop_words)
            dif_token=list(set(token_query) - set(stop_words))
            print("token_query----"+str(dif_token))
            fhandw.write(str(dif_token))
            #fhanddiffstop.write(str(dif_token))
        return self.name
