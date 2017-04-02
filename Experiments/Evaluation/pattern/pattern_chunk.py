#!/usr/bin/env python2
# -*- coding: utf-8 -*

from __future__ import division

import argparse,os,sys
from pattern.en import parse,pprint
from StringIO import StringIO

def patter_chunk(finput):

	with open(finput) as f:
		corpora = f.readlines()

	results=[]
	counter=0
	n_lines=len(corpora)

	#tokenize each line, pos-tag it and save in results
	for line in corpora:
		old_stdout = sys.stdout
		result = StringIO()
		sys.stdout = result

		print(parse(line,tokenize = True,			# Split punctuation marks from words?
								tags = False,					# Parse part-of-speech tags? (NN, JJ, ...)
								chunks = True,					# Parse chunks? (NP, VP, PNP, ...)
								relations = False,				# Parse chunk relations? (-SBJ, -OBJ, ...)
								lemmata = False,					# Parse lemmata? (ate => eat)
								encoding = 'utf-8'))			# Input string encoding.)

		sys.stdout = old_stdout
		chunk = result.getvalue()
		chunk=chunk.split(" ")

		#extract chunk
		for i in xrange(len(chunk)):
			chunk[i]=(chunk[i].split("/")[0],chunk[i].split("/")[2].rstrip("\n"))

		results+=[chunk]
		counter+=1
		print "Progress: ",str(counter)+"/"+str(n_lines),str(float(counter/n_lines)*100)+" %"	
	

	pattern_chunk_results=open("pattern_chunk_output.txt","w")
	for sentence in results:
		for token_chunk in sentence:
			# pattern_chunk_results.write(token_chunk[0]+" "+token_chunk[1].lower()+"\n")	#aritter
			pattern_chunk_results.write(token_chunk[0]+" "+token_chunk[1]+"\n")			#conll
		pattern_chunk_results.write("\n")
	pattern_chunk_results.close()

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='PATTERN CHUNK Task',epilog="CHUNKING with PATTERN.\n Each input file is a collection of sentences.\nEach line has a sentence or a set of sentences")
	parser.add_argument("-i","--input",nargs=1,help="Input filename",required=True)


	args=vars(parser.parse_args())
	finput=args['input'][0]

	if not os.path.isfile(finput): 
		print "File",freference,"not found"
		sys.exit() 

	patter_chunk(finput)





