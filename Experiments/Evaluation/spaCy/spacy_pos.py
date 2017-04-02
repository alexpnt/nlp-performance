#!/usr/bin/env python2
# -*- coding: utf-8 -*

from __future__ import division

import argparse,os,sys
from spacy.en import English
from StringIO import StringIO

def patter_pos(finput):

	with open(finput) as f:
		corpora = f.readlines()

	results=[]
	counter=0
	n_lines=len(corpora)

	nlp = English()

	#tokenize each line, pos-tag it and save in results
	for line in corpora:

		#process document
		doc = nlp(unicode(line.rstrip("\n"), "utf-8"))
		
		pos=[]
		for i in xrange(len(doc)):
			pos+=[(str(doc[i].text),doc[i].tag_)]

		results+=[pos]
		counter+=1
		print "Progress: ",str(counter)+"/"+str(n_lines),str(float(counter/n_lines)*100)+" %"	
	

	spacy_pos_results=open("spacy_pos_output.txt","w")
	for sentence in results:
		for token_pos in sentence:
			spacy_pos_results.write(token_pos[0]+" "+token_pos[1]+"\n")
		spacy_pos_results.write("\n")
	spacy_pos_results.close()

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='SPACY POS Task',epilog="POS with SPACY.\n Each input file is a collection of sentences.\nEach line has a sentence or a set of sentences")
	parser.add_argument("-i","--input",nargs=1,help="Input filename",required=True)


	args=vars(parser.parse_args())
	finput=args['input'][0]

	if not os.path.isfile(finput): 
		print "File",finput,"not found"
		sys.exit() 

	patter_pos(finput)





