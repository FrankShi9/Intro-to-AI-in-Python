import codecs
import os
import re
import numpy as np

from nltk.stem.porter import *
stemmer = PorterStemmer()
# plurals = ['caresses', 'flies', 'dies', 'mules', 'denied',
# 'died', 'agreed', 'owned', 'humbled', 'sized',
# 'meeting', 'stating', 'siezing', 'itemization',
# 'sensational', 'traditional', 'reference', 'colonizer',
# 'plotted']
# singles  = [stemmer.stem(plural) for plural in plurals]
# print(' '.join(singles))


texts = []
data_path = 'dataset/alt.atheism/'
path = 'dataset/'
fn = []

for fpath, dirs, fs in os.walk(path):
    for f in fs:
        filename = os.path.join(fpath, f)
        #print(filename)
        if not filename.endswith('.DS_Store'):
            fn.append(filename)

#for ele in os.listdir(data_path):
for ele in fn:
    #data = codecs.open(data_path+ele, 'r', encoding='Latin1')
    data = codecs.open(ele, 'r', encoding='Latin1')
    buf = re.split('[^a-zA-Z]',data.read())
    for elem in buf:
        #print(ele.lower())
        if elem != '':
            texts.append(elem.lower())
'''
#print(texts)
filename = 'RAW.txt'
with open(filename, 'w') as file_object:
    for ele in texts:
        file_object.write(ele+'\n')
'''

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

resultX = [stemmer.stem(text) for text in result ]
#print(result)
#print(resultX)


'''write file'''
# filename = 'ResultX.txt'
# with open(filename, 'w') as file_object:
#     for ele in resultX:
#         file_object.write(ele+'\n')


N = 2726


# print(set(resultX).__sizeof__()) #=2097352


resultND = []

#remove dup without changing order
for ele in resultX:
    if ele not in resultND:
        resultND.append(ele)



mat = np.zeros((2726,2097352), int)
# print(mat.__sizeof__())



def nk(inputFile, word):
    cnt = 0
    for ele in inputFile:
        if ele == word:
            cnt += 1

    return cnt

nK = np.zeros((1,2097352), int)


# print(np.shape(nK))


r , c = np.shape(nK)

for row in range(0,r):
     for column in range(0,c):
         nK[row,column] = nk(resultND, resultND[column])