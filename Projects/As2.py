import codecs
import os

from nltk.stem.porter import *

stemmer = PorterStemmer()

plurals = ['caresses ', 'flies ', 'dies ', 'mules ', 'denied ',
'died ', 'agreed ', 'owned ', 'humbled ', 'sized ',
'meeting ', 'stating ', 'siezing ', 'itemization ',
'sensational ', 'traditional ', 'reference ', 'colonizer ',
'plotted ']

singles  = [stemmer.stem(plural) for plural in plurals]

print(' '.join(singles))

data_path = 'dataset/alt.atheism/'
for ele in os.listdir(data_path):
    data = codecs.open(data_path+ele, 'r', encoding='Latin1')
    print(data.read())