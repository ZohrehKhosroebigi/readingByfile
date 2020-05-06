import os
import nltk
class Tokenization():
    def token(self,doc_name):
        if not os.path.exists("logs"):
            os.mkdir("logs")
        doc = open(doc_name, 'r', encoding='utf8')
        self.name=doc_name + 'token.txt'
        stop_words=open('logs/stopwords.txt','r',encoding='utf8')
        stop=[]
        for s in stop_words:
            stop.append(s)
        fhandw = open(self.name, 'w', encoding='utf8')
        tokenizer = nltk.RegexpTokenizer(r"\w+")
        stop_word_list=[]

        for line in doc:
            token_query = tokenizer.tokenize(line)
            if token_query  not in stop_word_list:
                print("token_query----"+str(token_query))
                fhandw.write(str(token_query))



        return self.name
