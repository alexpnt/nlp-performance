#!/usr/bin/env python2
# -*- coding: utf-8 -*

import subprocess,os,argparse
from StringIO import StringIO
import sys


STANDORD_POS="../../../Experiments/Evaluation/stanford_nlp/lib/stanford-postagger-full-2015-12-09/"

def stanford_nlp_pos(finput):

	with open(finput) as f:
		corpora = f.readlines()

	results=[]
	counter=0
	n_lines=len(corpora)

	#tokenize each line, pos-tag it and save in results
	for line in corpora:
		with open("message.txt", "w") as input_file:
			input_file.write(line)

		proc = subprocess.Popen(["java","-cp",STANDORD_POS+"stanford-postagger.jar:"+STANDORD_POS+"lib/*","-Xmx2g","edu.stanford.nlp.tagger.maxent.MaxentTagger","-model",STANDORD_POS+"models/english-left3words-distsim.tagger","-tokenize.whitespace","-ssplit.eolonly","-textFile","message.txt","-outputFormat","tsv"],stdout=subprocess.PIPE,stdin=subprocess.PIPE)
		pos=proc.communicate()[0].replace("\t"," ").split("\n")
		proc.stdin.close()


		pos = filter(None, pos) #remove empty strings from list
		for i in xrange(len(pos)):
			pos[i]=(pos[i].split(" ")[0],pos[i].split(" ")[1])

		results+=[pos]
		counter+=1
		print "Progress: ",str(counter)+"/"+str(n_lines),str(float(counter/n_lines)*100)+" %"


	#save results
	stanford_nlp_pos_results=open("stanford_nlp_pos_output.txt","w")
	for sentence in results:
		for token_pos in sentence:
			stanford_nlp_pos_results.write(token_pos[0]+" "+token_pos[1]+"\n")
		stanford_nlp_pos_results.write("\n")
	stanford_nlp_pos_results.close()

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='STANDORD NLP POS Task',epilog="POS with STANDORD NLP.\n Each input file is a collection of sentences.\nEach line has a sentence or a set of sentences")
	parser.add_argument("-i","--input",nargs=1,help="Input filename",required=True)

	args=vars(parser.parse_args())
	finput=args['input'][0]

	if not os.path.isfile(finput): 
		print "File",freference,"not found"
		sys.exit() 

	stanford_nlp_pos(finput)