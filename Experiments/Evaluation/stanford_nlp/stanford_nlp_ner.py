#!/usr/bin/env python2
# -*- coding: utf-8 -*

import subprocess,os,argparse
from StringIO import StringIO
import sys


STANDORD_NER="../../../Experiments/Evaluation/stanford_nlp/lib/stanford-ner-2015-12-09/"

def stanford_nlp_ner(finput):

	with open(finput) as f:
		corpora = f.readlines()

	results=[]
	counter=0
	n_lines=len(corpora)

	#tokenize each line, pos-tag it and save in results
	for line in corpora:
		with open("message.txt", "w") as input_file:
			input_file.write(line)

		proc = subprocess.Popen(["java","-cp",STANDORD_NER+"stanford-ner.jar:"+STANDORD_NER+"lib/*","-Xmx2g","edu.stanford.nlp.ie.crf.CRFClassifier","-loadClassifier",STANDORD_NER+"classifiers/english.all.3class.distsim.crf.ser.gz","-textFile","message.txt","-outputFormat","tsv"],stdout=subprocess.PIPE,stdin=subprocess.PIPE)
		pos=proc.communicate()[0].replace("\t"," ").split("\n")
		proc.stdin.close()


		pos = filter(None, pos) #remove empty strings from list
		for i in xrange(len(pos)):
			pos[i]=(pos[i].split(" ")[0],pos[i].split(" ")[1])

		results+=[pos]
		counter+=1
		print "Progress: ",str(counter)+"/"+str(n_lines),str(float(counter/n_lines)*100)+" %"


	#save results
	stanford_nlp_ner_results=open("stanford_nlp_ner_output.txt","w")
	for sentence in results:
		for token_pos in sentence:
			stanford_nlp_ner_results.write(token_pos[0]+" "+token_pos[1]+"\n")
		stanford_nlp_ner_results.write("\n")
	stanford_nlp_ner_results.close()

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='STANDORD NLP NER Task',epilog="NER with STANDORD NLP.\n Each input file is a collection of sentences.\nEach line has a sentence or a set of sentences")
	parser.add_argument("-i","--input",nargs=1,help="Input filename",required=True)

	args=vars(parser.parse_args())
	finput=args['input'][0]

	if not os.path.isfile(finput): 
		print "File",freference,"not found"
		sys.exit() 

	stanford_nlp_ner(finput)