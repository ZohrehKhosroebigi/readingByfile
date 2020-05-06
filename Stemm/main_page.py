from Stemm.Normalization import Normal
#from Persian_Normalization import Persian_Normalizer
from Stemm.Toeknization import Tokenization
from Stemm.Jacard import JacardSimilarity
from Stemm.Cosine import CosineSimilarity
from Stemm.stemm import Stemer_


persian_norm=Normal()
persian_norm.nomal('logs/doc.txt')
persian_token=Tokenization()
persian_token.token(persian_norm.name)

persian_norm1=Normal()
persian_norm1.nomal('logs/doc2.txt')
persian_token1=Tokenization()
persian_token1.token(persian_norm1.name)

"""persian_lemm=Lemmiz()
persian_lemm.lemmiz(persian_token.name,persian_token1.name)"""
persian_stem=Stemer_()
persian_stem.stem_(persian_token.name,persian_token1.name)

persian_jaccard=JacardSimilarity()
persian_jaccard.jacardsimilarity(persian_stem.name_stem_doc,persian_stem.name_stem_query)

persian_cosine=CosineSimilarity()
persian_cosine.cosinesimilarity(persian_stem.name_stem_doc,persian_stem.name_stem_query)



