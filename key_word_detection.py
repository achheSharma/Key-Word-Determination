import math
import re
import operator
import nltk
from nltk.book import *
from textblob import TextBlob
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords, gutenberg, brown, inaugural, webtext, reuters, state_union, abc, names

count_of_documents = 0

def stop_words():
    stop_words = set(stopwords.words('english'))

    ''' Include additional Stop Words '''
    # file1 = open("FoxStoplist.txt", 'r')
    # text = file1.readlines()
    # b = []
    # for i in text:
    #     b.append(i.strip())
    # FoxStoplist = set(b)

    # file1 = open("SmartStoplist.txt", 'r')
    # text = file1.readlines()
    # b = []
    # for i in text:
    #     b.append(i.strip())
    # SmartStoplist = set(b)
    # stop_words.union(FoxStoplist,SmartStoplist)

    return stop_words

def count_of_docs(corpuses):
    global count_of_documents
    if count_of_documents == 0:
        for i in corpuses:
            files = i.fileids()
            count_of_documents = count_of_documents + len(files)
    return count_of_documents

def IDF(corpuses, keyword, flag): #Inverse Document Frequency
    hit_count = 1
    for i in corpuses:
        if flag == 0:
            count_of_documents = count_of_docs(corpuses)
            for j in i.fileids():
                words = set(i.words(fileids = j))
                words = [w.lower() for w in words]
                if keyword in words:
                    hit_count = hit_count+1
        else:
            count_of_documents = len(corpuses[0])
            for j in i:
                words = set([w.lower() for w in j])
                if keyword in words:
                    hit_count = hit_count+1
    idf = math.log1p(count_of_documents/hit_count)
    return idf

categorized = [brown, reuters]
plaintext = [gutenberg, inaugural, names, webtext]
books = [text1, text2, text3, text4, text5, text6, text7, text8, text9]
# corpuses = categorized + plaintext
corpuses = [books]

''' Reading Input File '''
file = open("test.txt", 'r')
text = file.read()

words = word_tokenize(text)
words = [w.lower() for w in words]

count_of_words = len(words)
fd = nltk.FreqDist(words)

''' Blob Parsing '''
# blob = TextBlob(text)
# words = [n.lower() for n,t in blob.tags if t == 'NN' or t == 'NNP']

''' Stop Words Removal '''
stop_words = stop_words()
words = [w for w in words if w not in stop_words]
words = [w for w in words if w.isalpha() == True and len(w) > 1]
words = set(words)
words = list(words)

words_dict = {}
for i in words:
    words_dict[i] = 0

''' Find Keywords '''
for i in words:
    tf = fd[i]/count_of_words #Term Frequency
    idf = IDF(corpuses, i, 1) #Inverse Document Frequency
    if idf == math.inf:
        tf_idf = 1
    else:
        tf_idf = tf*idf
    words_dict[i] = tf_idf

sorted_words_dict = sorted(words_dict.items(), key=operator.itemgetter(1), reverse = True)

print(sorted_words_dict, "\n")

print("\nKeywords")
for i in range(len(sorted_words_dict)):
    if sorted_words_dict[0][1] - sorted_words_dict[i][1] > 0.5*sorted_words_dict[0][1]:
        break
    else:
        print(sorted_words_dict[i][0])