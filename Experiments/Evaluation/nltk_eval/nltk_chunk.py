#!/usr/bin/env python2
# -*- coding: utf-8 -*

from __future__ import division

import nltk
from nltk import word_tokenize,pos_tag,ne_chunk,data
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams

from nltk.corpus import conll2000

import argparse,os,sys

class UnigramChunker(nltk.ChunkParserI):
    def __init__(self, train_sents): # [_code-unigram-chunker-constructor]
        train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)]      # word,tag,chunk
                      for sent in train_sents]

        self.tagger = nltk.UnigramTagger(train_data) # [_code-unigram-chunker-buildit]

    def parse(self, sentence): # [_code-unigram-chunker-parse]
        pos_tags = [pos for (word,pos) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)

        tagged_iob_sentence=[]
        for i in xrange(len(sentence)):
        	tagged_iob_sentence+=[(sentence[i][0],tagged_pos_tags[i][1])]

        return tagged_iob_sentence


def nltk_chunk(finput,unigram_chunker):

	with open(finput) as f:
		corpora = f.readlines()

	results=[]
	counter=0
	n_lines=len(corpora)

	#tokenize each line, chunk-tag it and save in results
	for line in corpora:
		tokens = word_tokenize(line)	
		pos=pos_tag(tokens)
		counter+=1
	

		#write results
		nltk_chunk_results=open("nltk_chunk_output.txt","a")
		tagged_iob_sentence=unigram_chunker.parse(pos)
		for token_chunk in tagged_iob_sentence:
			if token_chunk[1] is None:
				nltk_chunk_results.write(token_chunk[0]+" O"+"\n")
			else:
				nltk_chunk_results.write(token_chunk[0]+" "+token_chunk[1]+"\n")
		nltk_chunk_results.write("\n")
		nltk_chunk_results.close()

		print "Progress: ",str(counter)+"/"+str(n_lines),str(float(counter/n_lines)*100)+" %"	

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='NLTK Chunking Task',epilog="Chunking with NLTK.\n Each input file is a collection of sentences.\nEach line has a sentence or a set of sentences")
	parser.add_argument("-i","--input",nargs=1,help="Input filename",required=True)


	args=vars(parser.parse_args())
	finput=args['input'][0]

	if not os.path.isfile(finput): 
		print "File",freference,"not found"
		sys.exit() 


	test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP','VP','PP'])
	train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP','VP','PP'])
	unigram_chunker = UnigramChunker(train_sents)
	nltk_chunk(finput,unigram_chunker)





