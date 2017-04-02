#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import division

from nltk import word_tokenize,pos_tag,ne_chunk,data
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams
from nltk.chunk import tree2conlltags
import codecs

import argparse,os,sys

def nltk_ner(finput):

	with codecs.open(finput,"r", "utf-8") as f:
		corpora = f.readlines()

	results=[]
	counter=0
	n_lines=len(corpora)
	#tokenize each line, pos-tag it, ner tag it and save in results
	for line in corpora:
		tokens = word_tokenize(line)	
		pos=pos_tag(tokens)

		# Loads the serialized NEChunkParser object
		chunker = data.load('chunkers/maxent_ne_chunker/english_ace_multiclass.pickle')
		maxEnt_classifier = chunker._tagger.classifier()
		maxEnt_labels=maxEnt_classifier.labels()
		ner=tree2conlltags(ne_chunk(pos,binary=False))
		
		results+=[ner]
		counter+=1

		nltk_ner_results=codecs.open("nltk_ner_output.txt","a","utf-8")
		for token_ner in ner:
			nltk_ner_results.write(token_ner[0]+" "+token_ner[2]+"\n")
		nltk_ner_results.write("\n")
		nltk_ner_results.close()
		print "Progress: ",str(counter)+"/"+str(n_lines),str(float(counter/n_lines)*100)+" %"	
	

	# nltk_ner_results=open("nltk_ner_output.txt","w")
	# for sentence in results:
	# 	for token_ner in sentence:
	# 		nltk_ner_results.write(token_ner[0]+" "+token_ner[2]+"\n")
	# 	nltk_ner_results.write("\n")
	# nltk_ner_results.close()

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='NLTK NER Task',epilog="NER with NLTK.\n Each input file is a collection of sentences.\nEach line has a sentence or a set of sentences")
	parser.add_argument("-i","--input",nargs=1,help="Input filename",required=True)


	args=vars(parser.parse_args())
	finput=args['input'][0]

	if not os.path.isfile(finput): 
		print "File",freference,"not found"
		sys.exit() 

	nltk_ner(finput)




