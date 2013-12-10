#coding:utf-8
import sys, os, time
import nltk
from nltk.corpus import gutenberg
from nltk.corpus import webtext
from nltk.corpus import nps_chat
from nltk.corpus import brown
from nltk.corpus import reuters
from nltk.corpus import inaugural
from nltk.corpus import udhr
"""
1. What are some useful text corpora and lexical resources, and how can we access
them with Python?
2. Which Python constructs are most helpful for this work?
3. How do we avoid repeating ourselves when writing Python code?
"""
#print dir(gutenberg)
for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
#    print int(num_chars/num_words), int(num_words/num_sents), int(num_words/num_vocab),fileid

#print dir(webtext)
#print help(webtext)
#print webtext.open('e:/nltk/test.txt')
#for fileid in webtext.fileids():
#    print fileid, webtext.raw(fileid)[:70]

#print dir(nps_chat)
#print help(nps_chat)
#chatroom = nps_chat.posts('10-19-20s_706posts.xml')
#print chatroom[123]

#stylistics
#print dir(brown)
#print help(brown)
#brown.categories()

"""
Choose a different section of the Brown Corpus, and adapt
the preceding example to count a selection of wh words, such as what,
when, where, who and why
"""
#news_text = brown.words(categories='news')
#news_text = brown.words(categories='humor')
#[w.lower() for w in news_text]
#fdist = nltk.FreqDist([w.lower() for w in news_text])
##modals = ['can', 'could', 'may', 'might', 'must', 'will']
#modals = ['what', 'when', 'where', 'who', 'why']
#for m in modals:
#    print m + ':', fdist[m]
#    
#
#cfd = nltk.ConditionalFreqDist(
#        (genre, word)
#        for genre in brown.categories()
#        for word in brown.words(categories=genre))
#genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
#modals = ['can', 'could', 'may', 'might', 'must', 'will']
#cfd.tabulate(conditions=genres, samples=modals)


#print reuters.fileids('corn')
#reuters.categories()
#print reuters.categories(['training/10027', 'training/9880'])


#print inaugural.fileids()
#print help(nltk.ConditionalFreqDist)

"""
do not work
"""
#cfd = nltk.ConditionalFreqDist(
#        (target, file[:4])
#         for fileid in inaugural.fileids()
#         for w in inaugural.words(fileid)
#         for target in ['america', 'citizen']
#         if w.lower().startswith(target))
#cfd.plot()

#print nltk.corpus.udhr.fileids()[:50]


#languages = ['Chickasaw', 'English', 'German_Deutsch',
#'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
#cfd = nltk.ConditionalFreqDist(
#(lang, len(word))
#for lang in languages
#for word in udhr.words(lang + '-Latin1'))
#cfd.plot(cumulative=True)


"""
Loading Your Own Corpus
"""
#1
#from nltk.corpus import PlaintextCorpusReader
#corpus_root = 'e:/nltk'
#wordlists = PlaintextCorpusReader(corpus_root, '.*')
#print wordlists.fileids()
#print wordlists.sents('ch2.py')
#
#2
#from nltk.corpus import BracketParseCorpusReader
#corpus_root = r"C:\corpora\penntreebank\parsed\mrg\wsj"
#file_pattern = r".*/wsj_.*\.mrg"
#ptb = BracketParseCorpusReader(corpus_root, file_pattern)
#ptb.fileids()
#len(ptb.sents())

