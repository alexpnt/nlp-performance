#!/usr/bin/env python2
# -*- coding: utf-8 -*

from __future__ import division

import argparse,os,sys
from spacy.en import English
from StringIO import StringIO

def patter_chunk(finput):

	with open(finput) as f:
		corpora = f.readlines()

	results=[]
	counter=0
	n_lines=len(corpora)

	nlp = English()

	#tokenize each line, chunk-tag it and save in results
	for line in corpora:

		#process document
		doc = nlp(unicode(line.rstrip("\n"), "utf-8"))
		
		#init
		chunks=[]
		for i in xrange(len(doc)):
			chunks+=[[str(doc[i].text),'O']]

		#NP chunks
		for chunk in doc.noun_chunks:
			# print chunk.label_, chunk.orth_,chunk.start,chunk.end, '<--', chunk.root.head.orth_
			for i in xrange(chunk.start,chunk.end):
				chunks[i][1]='I-'+str(chunk.label_)
			chunks[chunk.start][1]='B-'+str(chunk.label_)

		results+=[chunks]
		counter+=1
		print "Progress: ",str(counter)+"/"+str(n_lines),str(float(counter/n_lines)*100)+" %"	
	

	spacy_chunk_results=open("spacy_chunk_output.txt","w")
	for sentence in results:
		for token_chunk in sentence:
			spacy_chunk_results.write(token_chunk[0]+" "+token_chunk[1]+"\n")
		spacy_chunk_results.write("\n")
	spacy_chunk_results.close()

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='SPACY CHUNK Task',epilog="CHUNK with SPACY.\n Each input file is a collection of sentences.\nEach line has a sentence or a set of sentences")
	parser.add_argument("-i","--input",nargs=1,help="Input filename",required=True)


	args=vars(parser.parse_args())
	finput=args['input'][0]

	if not os.path.isfile(finput): 
		print "File",finput,"not found"
		sys.exit() 

	patter_chunk(finput)





