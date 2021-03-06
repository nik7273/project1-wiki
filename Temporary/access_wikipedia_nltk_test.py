import nltk, matplotlib, numpy, pylab, string, codecs

import matplotlib.pyplot as plt 
import Graphics as artist

"from nltk.stem.porter import *"
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop = stopwords.words('english')
filename = '../data.txt'
READ = 'rb'
WRITE = 'wb'
measures = ['cm', 'in', 'mg', 'lb', 'kg', 'mm', 'ft']
lemma = nltk.WordNetLemmatizer()
punkt = set(string.punctuation)
data = [word.lower() for word in word_tokenize(open(filename,READ).read()) if word not in punkt]
data = [lemma.lemmatize(word) for word in data]
data = [word for word in data if word not in stop]
data = [word for word in data if word not in measures]
with open('WIKI_words',WRITE) as outfile:
    for word in data:
        print>>outfile,word
      


distri1 = nltk.FreqDist(open('WIKI_words',READ).read().splitlines())

common = distri1.most_common(30)

words,freqs = zip(*common)



with codecs.open("listedData.txt",WRITE,'utf-8') as outfile:
    for x,y in common:
        print>>outfile, "%s %s" % (y, x)


fig = plt.figure()
ax = fig.add_subplot(111)
ax.semilogy(freqs,'k--',linewidth=3)
artist.adjust_spines(ax)

ax.set_xticks(xrange(len(words)))
ax.set_xticklabels([r'\textbf{\textsc{%s}'%word for word in words],rotation='vertical')
ax.set_ylabel(artist.format("Word Count"))

plt.tight_layout()
plt.show()
plt.savefig("wikipedia-word-frequencies.png", bbox_inches="tight")
