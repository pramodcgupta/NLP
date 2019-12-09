# -*- coding: utf-8 -*-
"""
Pramodkumar Gupta
Tokenize Code
"""

import nltk

#nltk.download('punkt')

paragraph = """The Republic of India has two principal short names in both official and popular English usage, each of which is historically significant, India and Bharat. 
 The first article of the Constitution of India states that India, that is Bharat, shall be a union of states, implicitly codifying India and Bharat as equally official short names for the Republic of India. 
 A third name, Hindustan, is sometimes an alternative name for the region comprising most of the modern Indian states of the subcontinent when Indians speak among themselves. 
 The usage of Bharat, Hindustan, or India depends on the context and language of conversation. 
 the name for India in several Indian languages, is variously said to be derived from the name of either Dushyantas son Bharata or Rishabhas son Bharata. 
 At first the name Bharata referred only to the western part of the Gangetic Valley in North India, but was later more broadly applied to the Indian subcontinent and the region of Greater India, as was the name India.
 Today it refers to the contemporary Republic of India located therein. The name India is originally derived from the name of the river Sindhu (Indus River)  and has been in use in Greek since Herodotus (4th century BCE). 
 The term appeared in Old English as early the 9th century and reemerged in Modern English in the 17th century."""

# Tokenize sentences
sentences = nltk.sent_tokenize(paragraph)

# Tokenize words
words = nltk.word_tokenize(paragraph)

print(sentences)
print(words)
