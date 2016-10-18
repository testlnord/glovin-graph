# coding: utf-8
import glove
c = glove.Corpus()
c.fit(["dog eat food", "people eat food", "dog eat people"], window=3)
c.fit([["dog", "eat", "food"], ["people eat food", "dog eat people"], window=3)
c
]
c.fit([["dog", "eat", "food"], ["people eat food", "dog eat people"]], window=3)
c
c.matrix
c.fit([["dog", "eat", "food"], ["people", "eat", "food"], ["dog", "eat", "people"]], window=3)
c.matrix
c.matrix[1]
c.matrix.to_array()
c.matrix.toarray()
c.fit([["dog", "eat", "food"], ["people", "eat", "food"], ["dog", "eat", "people"]], window=3)
s = glove.Glove(2, 0.05)
s.fit(c.matrix, epochs = 10, no_threads = 1, verbose = True)
s.add_dictionary(c.dictionary)
c.dictionary
c = glove.Corpus()
c.fit([["dog", "eat", "food"], ["people", "eat", "food"], ["dog", "eat", "people"]], window=3)
c.dictionary
s.fit(c.matrix, epochs = 10, no_threads = 1, verbose = True)
s = glove.Glove(2, 0.05)
s.fit(c.matrix, epochs = 10, no_threads = 1, verbose = True)
s.add_dictionary(c.dictionary)
glove.most_similar('dog')
s.most_similar('dog')
c.matrix.toarray
c.matrix.toarray()
c.dictionary
get_ipython().magic(u'save all_today_session')
