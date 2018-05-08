''' Create Lemmatized Sets of Books in NLTK '''

from nltk.book import *
from nltk.stem.wordnet import WordNetLemmatizer

path = "C:\\Users\\aksha\\Desktop\\Key Word Detection\\Books\\"

books = [text1, text2, text3, text4, text5, text6, text7, text8, text9]
files = ["Book1.txt", "Book2.txt", "Book3.txt", "Book4.txt", "Book5.txt", "Book6.txt", "Book7.txt", "Book8.txt", "Book9.txt"]

lmtzr = WordNetLemmatizer()

for i in range(len(books)):
	words = set([lmtzr.lemmatize(w.lower()) for w in books[i] if w.isalpha() == True])
	words = ' '.join(words)
	file = open(path + files[i], 'w')
	file.write(words)
	file.close()
	print(files[i])