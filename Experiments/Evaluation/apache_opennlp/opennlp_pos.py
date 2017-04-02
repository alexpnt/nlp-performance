#!/usr/bin/env python2
# -*- coding: utf-8 -*

import subprocess,os,argparse
from StringIO import StringIO
import sys

OPENNLP_DIR="../../../Experiments/Tools/apache-opennlp-1.6.0/"

def opennlp_pos(finput):

	with open(finput) as f:
		corpora = f.readlines()

	results=[]
	counter=0
	n_lines=len(corpora)

	#tokenize each line, pos-tag it and save in results
	for line in corpora:

		proc = subprocess.Popen([OPENNLP_DIR+"bin/opennlp",'TokenizerME',OPENNLP_DIR+'models/en-token.bin'],stdout=subprocess.PIPE,stdin=subprocess.PIPE)
		proc.stdin.write(line)
		tokenized_line=proc.communicate()[0]

		# proc = subprocess.Popen([OPENNLP_DIR+"bin/opennlp",'POSTagger',OPENNLP_DIR+'models/en-pos-maxent.bin'],stdout=subprocess.PIPE,stdin=subprocess.PIPE)
		proc = subprocess.Popen([OPENNLP_DIR+"bin/opennlp",'POSTagger',OPENNLP_DIR+'models/en-pos-perceptron.bin'],stdout=subprocess.PIPE,stdin=subprocess.PIPE)
		
		proc.stdin.write(tokenized_line)
		pos=proc.communicate()[0]
		pos=pos.split(" ")
		for i in xrange(len(pos)):
			underscore=pos[i].rindex('_')
			token=pos[i][:underscore]
			tag=pos[i][underscore+1:].rstrip("\n")
			pos[i]=(token,tag)
		

		results+=[pos]
		counter+=1
		print "Progress: ",str(counter)+"/"+str(n_lines),str(float(counter/n_lines)*100)+" %"	
		
	
	#save results
	opennlp_pos_results=open("opennlp_pos_output.txt","w")
	for sentence in results:
		for token_pos in sentence:
			opennlp_pos_results.write(token_pos[0]+" "+token_pos[1]+"\n")
		opennlp_pos_results.write("\n")
	opennlp_pos_results.close()

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='OPENNLP POS Task',epilog="POS with OPENNLP.\n Each input file is a collection of sentences.\nEach line has a sentence or a set of sentences")
	parser.add_argument("-i","--input",nargs=1,help="Input filename",required=True)


	args=vars(parser.parse_args())
	finput=args['input'][0]

	if not os.path.isfile(finput): 
		print "File",freference,"not found"
		sys.exit() 

	opennlp_pos(finput)
