#!/usr/bin/env python2
# -*- coding: utf-8 -*

from __future__ import division

import argparse,os,sys
from pattern.en import parse,pprint
from StringIO import StringIO

def patter_pos(finput):

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
								tags = True,					# Parse part-of-speech tags? (NN, JJ, ...)
								chunks = False,					# Parse chunks? (NP, VP, PNP, ...)
								relations = False,				# Parse chunk relations? (-SBJ, -OBJ, ...)
								lemmata = False,					# Parse lemmata? (ate => eat)
								encoding = 'utf-8'))			# Input string encoding.)

		sys.stdout = old_stdout
		pos = result.getvalue()
		pos=pos.split(" ")

		#extract pos
		for i in xrange(len(pos)):
			pos[i]=(pos[i].split("/")[0],pos[i].split("/")[1].rstrip("\n"))

		results+=[pos]
		counter+=1
		print "Progress: ",str(counter)+"/"+str(n_lines),str(float(counter/n_lines)*100)+" %"	
	

	pattern_pos_results=open("pattern_pos_output.txt","w")
	for sentence in results:
		for token_pos in sentence:
			pattern_pos_results.write(token_pos[0]+" "+token_pos[1]+"\n")
		pattern_pos_results.write("\n")
	pattern_pos_results.close()

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='PATTERN POS Task',epilog="POS with PATTERN.\n Each input file is a collection of sentences.\nEach line has a sentence or a set of sentences")
	parser.add_argument("-i","--input",nargs=1,help="Input filename",required=True)


	args=vars(parser.parse_args())
	finput=args['input'][0]

	if not os.path.isfile(finput): 
		print "File",freference,"not found"
		sys.exit() 

	patter_pos(finput)





