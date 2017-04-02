#!/usr/bin/env python2
# -*- coding: utf-8 -*

from __future__ import division

from nltk import word_tokenize,pos_tag,ne_chunk,data
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams

import argparse,os,sys

def nltk_pos(finput):

	with open(finput) as f:
		corpora = f.readlines()

	results=[]
	counter=0
	n_lines=len(corpora)

	#tokenize each line, pos-tag it and save in results
	for line in corpora:
		tokens = word_tokenize(line)	
		pos=pos_tag(tokens)
		results+=[pos]
		counter+=1
		print "Progress: ",str(counter)+"/"+str(n_lines),str(float(counter/n_lines)*100)+" %"	
	

	nltk_pos_results=open("nltk_pos_output.txt","w")
	for sentence in results:
		for token_pos in sentence:
			nltk_pos_results.write(token_pos[0]+" "+token_pos[1]+"\n")
		nltk_pos_results.write("\n")
	nltk_pos_results.close()

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='NLTK POS Task',epilog="POS with NLTK.\n Each input file is a collection of sentences.\nEach line has a sentence or a set of sentences")
	parser.add_argument("-i","--input",nargs=1,help="Input filename",required=True)


	args=vars(parser.parse_args())
	finput=args['input'][0]

	if not os.path.isfile(finput): 
		print "File",freference,"not found"
		sys.exit() 

	nltk_pos(finput)





