import codecs
import os
import re
import numpy as np
np.set_printoptions(threshold=np.inf)
# np.set_printoptions(threshold=10)
import math
from nltk.stem.porter import *
import pprint

stemmer = PorterStemmer()
# plurals = ['caresses', 'flies', 'dies', 'mules', 'denied',
# 'died', 'agreed', 'owned', 'humbled', 'sized',
# 'meeting', 'stating', 'siezing', 'itemization',
# 'sensational', 'traditional', 'reference', 'colonizer',
# 'plotted']
# singles  = [stemmer.stem(plural) for plural in plurals]
# print(' '.join(singles))

texts = []
# data_path = 'dataset/alt.atheism/51060'
path = 'dataset/'
fn = []

for fpath, dirs, fs in os.walk(path):
    for f in fs:
        filename = os.path.join(fpath, f)
        #print(filename)
        if not filename.endswith('.DS_Store'):
            fn.append(filename)

print(len(fn),' files') #2726
# print(fn)

# print('fn: \n', fn)
#for ele in os.listdir(data_path):
for ele in fn:
    #data = codecs.open(data_path+ele, 'r', encoding='Latin1')
    data = codecs.open(ele, 'r', encoding='Latin1')
    buf = re.split('[^a-zA-Z]',data.read())
    for elem in buf:
        #print(ele.lower())
        if elem != '':
            texts.append(elem.lower())
# pprint.pprint(texts, compact=True)
# print('texts: \n', texts)
    #data = codecs.open(data_path+ele, 'r', encoding='Latin1')
# data = codecs.open(data_path, 'r', encoding='Latin1')
# buf = re.split('[^a-zA-Z]',data.read())
# for elem in buf:
#     #print(ele.lower())
#     if elem != '':
#         texts.append(elem.lower())


# #print(texts)
# filename = 'RAW.txt'
# with open(filename, 'w') as file_object:
#     for ele in texts:
#         file_object.write(ele+'\n')


stop_words_path = 'stopwords.txt'
stop_words = set()
for ele in open(stop_words_path,'r', encoding="utf8"):
    stop_words.add(ele.strip('\n'))

# print('stop_words: \n', stop_words, end=' ')


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

# print('result: \n', result)

# stemmer
resultX = [stemmer.stem(text) for text in result]

# print('resultX: \n', resultX)
# check stopwords again
resultK = []
det = False
for ele in resultX:
    det = False
    for x in stop_words:
        if ele == x:
            det = True
            continue
    if det == False:
        resultK.append(ele)
# pprint.pprint(resultK, width=100, compact=True)
# print(len(resultK))
# print('resultK: \n', resultK[:20], ' ... ', resultK[362220:])
#print(result)
#print(resultX)

# '''write file'''
# filename = 'Result.txt'
# with open(filename, 'w') as file_object:
#     for ele in result:
#         file_object.write(ele+'\n')
#
# '''write file'''
# filename = 'ResultK.txt'
# with open(filename, 'w') as file_object:
#     for ele in resultK:
#         file_object.write(ele+'\n')
#
#
# N = 2726
# # resultSet = list(set(resultX))
# # print(len(resultSet)) #32931
# resultND = []
#
# #remove dup without changing order
# for ele in resultK:
#     if ele not in resultND:
#         resultND.append(ele)
#
# # print(np.shape(resultND)) #22975
# # print('resultND: \n', resultND)
#
# textM = [[] for i in range (0,2726)]
# i = 0
# #for ele in os.listdir(data_path):
# for ele in fn:
#     data = codecs.open(ele, 'r', encoding='Latin1')
#     buf = re.split('[^a-zA-Z]',data.read())
#     for elem in buf:
#         if elem != '':
#             textM[i].append(elem.lower())
#     i += 1
#
# # print('textM: \n', textM)
#
# resultm = [[] for i in range (0,2726)]
# i = 0
# det = False
# for i in range(0, 2726):
#     for ele in textM[i]:
#         det = False
#         for x in stop_words:
#             if ele == x:
#                 det = True
#                 continue
#         if det == False:
#             resultm[i].append(ele)
#     i += 1
#
# # print('resultm: \n', resultm)
#
# resultM = [[] for i in range (0,2726)]
# i = 0
# for i in range(0, 2726):
#     for ele in resultm[i]:
#         resultM[i].append(stemmer.stem(ele))
#     i += 1
#
# # print('resultM: \n', resultM)
#
# resultMK =  [[] for i in range (0,2726)]
# i = 0
# det = False
# for i in range(0, 2726):
#     for ele in resultM[i]:
#         det = False
#         for x in stop_words:
#             if ele == x:
#                 det = True
#                 continue
#         if det == False:
#             resultMK[i].append(ele)
#     i += 1
#
# # print('resultMK: \n', resultMK)
#
# def nk(inputFile, word): #document frequency for a given word
#     cnt = 0
#     for i in range(0, 2726):
#         if word in inputFile[i]:
#             cnt += 1
#
#     return cnt
#
#
# nK = np.zeros((22975,1), int) # the matrix to store document frequency
#
#
# # print(np.shape(nK))
#
#
# r , c = np.shape(nK)
#
# for row in range(0,r): # store the nk value for each unique word in the dataset
#          nK[row, 0] = ((float) (N)/(nk(resultMK, resultND[row])))
#
# # print('nK: \n',nK)
# # filename = 'nK.txt'
# # with open(filename, 'w') as f:
# #     print('nK:\n', nK, sep='    ', file=f)
# print('50%')
#
# fK = np.zeros((2726,22975), int) # matrix to store the frequency of word i in doc k
#
#
# def fk(inputFile, word):
#     cnt = 0
#     for ele in inputFile:
#         if ele == word:
#             cnt += 1
#
#     return cnt
#
# r , c = np.shape(fK)
#
# for row in range(0,r):
#      for column in range(0,c):
#          fK[row, column] = fk(resultMK[row], resultND[column])
#
#
# # print('fK: \n',fK)
# # filename = 'fK.txt'
# # with open(filename, 'w') as f:
# #     print('fK:\n', fK, sep='    ', file=f)
# # print('60%')
#
# aK = np.zeros((2726,22975), float)
# r , c = np.shape(fK)
#
# for row in range(0,r):
#     for column in range(0,c):
#         aK[row, column] = fK[row, column]*math.log2(nK[column, 0])
#
# # print('aK: \n',aK)
# # filename = 'aK.txt'
# # with open(filename, 'w') as f:
# #     print('aK:\n', aK, sep='    ', file=f)
# # print(aK[0,0])
# print('70%')
#
# sigma = np.zeros((2726,1), float)
#
# r , c = np.shape(sigma)
# sum = 0
# for row in range(0,r):
#     sum = 0
#     for i in range(0,22975):
#         sum += (aK[row, i]**2)
#     sigma[row, 0] = math.sqrt(sum)
# # print('sigma: \n',sigma)
#
# # filename = 'sigma.txt'
# # with open(filename, 'w') as f:
# #     print('sigma:\n', sigma, sep='    ', file=f)
#
# print('80%')
#
# AK = np.zeros((2726,22975), float)
# r , c = np.shape(AK)
# # print((float)(aK[0, 0])/sigma[0, 0])
#
# for row in range(0,r):
#     for column in range(0,c):
#         AK[row, column] = (((float)(aK[row, column]))/sigma[row, 0])
#
# # print('90%')
# # print('AK: \n', AK)
#
# # filename = 'AK.txt'
# # with open(filename, 'w') as f:
# #     print('AK:\n', AK, sep='    ', file=f)
# # print('95%')
#
# # np.savez('train-20ng.npz',X=AK)
# # print('100%')
