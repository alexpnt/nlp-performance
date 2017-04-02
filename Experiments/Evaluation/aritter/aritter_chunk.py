#!/usr/bin/env python2
# -*- coding: utf-8 -*

from __future__ import division

import argparse,os,sys,subprocess

ARITTER_DIR="../.../../Experiments/Tools/aritter-twitter-nlp/"
os.environ['TWITTER_NLP'] = ARITTER_DIR

def cutoff(string, pattern):
		idx = string.find(pattern)
		return string[:idx if idx != -1 else len(string)]

def aritter_chunk(finput):

	with open(finput) as f:
		corpora = f.readlines()

	results=[]
	counter=0
	n_lines=len(corpora)

	#tokenize each line, pos-tag it and save in results
	for line in corpora:
		# proc = subprocess.Popen(["python2",ARITTER_DIR+"python/ner/extractEntities2.py",'--classify','--pos','--chunk'],stdout=subprocess.PIPE,stdin=subprocess.PIPE)
		proc = subprocess.Popen(["python2",ARITTER_DIR+"python/ner/extractEntities2.py",'--pos','--chunk'],stdout=subprocess.PIPE,stdin=subprocess.PIPE)
		proc.stdin.write(line)
		ner=proc.communicate()[0]
		ner=cutoff(ner,"Average time per tweet")
		ner=ner.split(" ")

		#extract chunks
		for i in xrange(len(ner)):
			print ner[i]
			ner[i]=(ner[i].split("/")[0],ner[i].split("/")[3].rstrip("\n"))

		results+=[ner]
		counter+=1
		print "Progress: ",str(counter)+"/"+str(n_lines),str(float(counter/n_lines)*100)+" %"	
	

	aritter_chunk_results=open("aritter_chunk_output.txt","w")
	for sentence in results:
		for token_pos in sentence:
			aritter_chunk_results.write(token_pos[0]+" "+token_pos[1].lower()+"\n")
		aritter_chunk_results.write("\n")
	aritter_chunk_results.close()

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='Aritter POS Task',epilog="CHUNK with Aritter.\n Each input file is a collection of sentences.\nEach line has a sentence or a set of sentences")
	parser.add_argument("-i","--input",nargs=1,help="Input filename",required=True)


	args=vars(parser.parse_args())
	finput=args['input'][0]

	if not os.path.isfile(finput): 
		print "File",freference,"not found"
		sys.exit() 

	aritter_chunk(finput)





