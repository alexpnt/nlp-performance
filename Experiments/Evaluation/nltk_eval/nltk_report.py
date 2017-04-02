#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import nltk

# Loads the serialized NEChunkParser object
chunker = nltk.data.load('chunkers/maxent_ne_chunker/english_ace_multiclass.pickle')

# The MaxEnt classifier
maxEnt = chunker._tagger.classifier()

def maxEnt_report():

    # The MaxEnt classifier
    maxEnt = chunker._tagger.classifier()
    print 'These are the labels used by the NLTK\'s NEC...'
    print maxEnt.labels()
    print ''

    print 'These are the most informative features found in the ACE corpora...'
    maxEnt.show_most_informative_features()

def ne_report(sentence, report_all=False):

    # Convert the sentence into a tokens with their POS tags
    tokens = nltk.word_tokenize(sentence)
    tokens = nltk.pos_tag(tokens)

    tags = []
    for i in range(0, len(tokens)):
        featureset = chunker._tagger.feature_detector(tokens, i, tags)
        tag = chunker._tagger.choose_tag(tokens, i, tags)
        if tag != 'O' or report_all:
            print '\nExplanation on the why the word \'' + tokens[i][0] + '\' was tagged:'
            featureset = chunker._tagger.feature_detector(tokens, i, tags)
            maxEnt.explain(featureset)
        tags.append(tag)

if __name__ == '__main__':
	maxEnt_report()
