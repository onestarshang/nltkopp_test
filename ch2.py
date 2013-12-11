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



#print genre_word[:10]
#print len(genre_word)
#print brown.words(categories = 'news')[:10]

#cfd = nltk.ConditionalFreqDist(genre_word)
#print cfd
#print list(cfd['romance'])

#genre_word = [(genre, word)
#for genre in ['news', 'romance']
#for word in brown.words(categories=genre)]
"""
my turn...
"""
#days = ['Sunday', 'Monday', 'Tuseday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
#cfd = nltk.ConditionalFreqDist(genre_word)
#print list(cfd['news']['Sunday'])
#list(cfd['news'])
#list(cfd['romance'])
#print cfd['news']['Sunday']
#print cfd['romance']['Sunday']
#cfd.tabulate(conditions = ['news', 'romance'], samples = days, cumulative=True)

#def generate_model(cfdist, word, num=15):
#    for i in range(num):
#        print word,
#        word = cfdist[word].max()
#text = nltk.corpus.genesis.words('english-kjv.txt')
#bigrams = nltk.bigrams(text)
#cfd = nltk.ConditionalFreqDist(bigrams)
#print cfd['living']
#generate_model(cfd, 'good')
#

"""
wordNet
"""
from nltk.corpus import wordnet as wn
#print wn.synsets('motorcar')
#print wn.synset('car.n.01').lemma_names
#print wn.synset('car.n.01').definition
#print wn.synset('car.n.01').examples
#
#wn.synset('car.n.01').lemmas #get all the lemmas for a given synset
#wn.lemma('car.n.01.automobile') #look up a particular lemma
#wn.lemma('car.n.01.automobile').synset #get the synset corresponding to a lemma
#wn.lemma('car.n.01.automobile').name #get the “name” of a lemma
#
#wn.synsets('car')

#motorcar = wn.synset('car.n.01')
#types_of_motorcar = motorcar.hyponyms()
#types_of_motorcar[26]
#print sorted([lemma.name for synset in types_of_motorcar for lemma in synset.lemmas])
#
#for synset in wn.synsets('dish'):
#    print synset.lemma_names


"""
上下位词、同义词、反义词.....
Hypernyms and hyponyms are called lexical relations because they relate one synset
to another. These two relations navigate up and down the “is-a” hierarchy. Another
important way to navigate the WordNet network is from items to their components
(meronyms)转义 or to the things they are contained in (holonyms)整体词.
"""

#wn.synset('tree.n.01').part_meronyms()
#wn.synset('walk.v.01').entailments() #同义词
#wn.lemma('staccato.r.01.staccato').antonyms() #反义词
#
#"""
#Of course we know that whale is very specific (and baleen whale even more so), whereas
#vertebrate is more general and entity is completely general. We can quantify this concept
#of generality by looking up the depth of each synset:
#"""
#wn.synset('baleen_whale.n.01').min_depth()
#wn.synset('whale.n.02').min_depth()
#wn.synset('vertebrate.n.01').min_depth()
#wn.synset('entity.n.01').min_depth()
#
"""
SUMMARY

• A text corpus is a large, structured collection of texts. NLTK comes with many
corpora, e.g., the Brown Corpus, nltk.corpus.brown.
• Some text corpora are categorized, e.g., by genre or topic; sometimes the categories
of a corpus overlap each other.
• A conditional frequency distribution is a collection of frequency distributions, each
one for a different condition. They can be used for counting word frequencies,
given a context or a genre.
• Python programs more than a few lines long should be entered using a text editor,
saved to a file with a .py extension, and accessed using an import statement.
• Python functions permit you to associate a name with a particular block of code,
and reuse that code as often as necessary.
• Some functions, known as “methods,” are associated with an object, and we give
the object name followed by a period followed by the method name, like this:
x.funct(y), e.g., word.isalpha().
• To find out about some variable v, type help(v) in the Python interactive interpreter
to read the help entry for this kind of object.
• WordNet is a semantically oriented dictionary of English, consisting of synonym
sets—or synsets—and organized into a network.
• Some functions are not available by default, but must be accessed using Python’s
import statement.
"""
"""
TEST

25. ● Define a function find_language() that takes a string as its argument and returns
a list of languages that have that string as a word. Use the udhr corpus and limit
your searches to files in the Latin-1 encoding.
26. ● What is the branching factor of the noun hypernym hierarchy? I.e., for every
noun synset that has hyponyms—or children in the hypernym hierarchy—how
many do they have on average? You can get all noun synsets using wn.all_syn
sets('n').
27. ● The polysemy of a word is the number of senses it has. Using WordNet, we can
determine that the noun dog has seven senses with len(wn.synsets('dog', 'n')).
Compute the average polysemy of nouns, verbs, adjectives, and adverbs according
to WordNet.
28. ● Use one of the predefined similarity measures to score the similarity of each of
the following pairs of words. Rank the pairs in order of decreasing similarity. How
close is your ranking to the order given here, an order that was established experimentally
by (Miller & Charles, 1998): car-automobile, gem-jewel, journey-voyage,
boy-lad, coast-shore, asylum-madhouse, magician-wizard, midday-noon, furnacestove,
food-fruit, bird-cock, bird-crane, tool-implement, brother-monk, ladbrother,
crane-implement, journey-car, monk-oracle, cemetery-woodland, foodrooster,
coast-hill, forest-graveyard, shore-woodland, monk-slave, coast-forest,
lad-wizard, chord-smile, glass-magician, rooster-voyage, noon-string.
"""
