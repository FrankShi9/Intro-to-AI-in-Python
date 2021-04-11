import codecs
import os
import re
from nltk.stem import *
#bug here!
'''
from nltk.stem.porter import *
stemmer = PorterStemmer()
plurals = ['caresses ', 'flies ', 'dies ', 'mules ', 'denied ',
'died ', 'agreed ', 'owned ', 'humbled ', 'sized ',
'meeting ', 'stating ', 'siezing ', 'itemization ',
'sensational ', 'traditional ', 'reference ', 'colonizer ',
'plotted ']
singles  = [stemmer.stem(plural) for plural in plurals]
print(' '.join(singles))
'''

texts = []
data_path = 'dataset/alt.atheism/'
for ele in os.listdir(data_path):
    data = codecs.open(data_path+ele, 'r', encoding='Latin1')
    buf = re.split('[^a-zA-z]',data.read())
    for ele in buf:
        #print(ele.lower())
        texts.append(ele.lower())

#print(texts)

stop_words_path = 'stopwords.txt'
stop_words = set()
for ele in open(stop_words_path,'r', encoding="utf8"):
    stop_words.add(ele.strip('\n'))
#print(stop_words)
texts_all_alpha = []
for ele in texts:
    if ele != '':
        texts_all_alpha.append(ele)
#print(texts_all_alpha)


result = []
det = False
for ele in texts:
    det = False
    for x in stop_words:
        if ele == x:
            det = True
            continue
    if det == False:
        result.append(ele)


print(result)
