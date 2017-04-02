#!/usr/bin/env python2
# -*- coding: utf-8 -*

import subprocess,os,argparse
from StringIO import StringIO
import sys

CMU_ARK_DIR="../../../Experiments/Tools/ark-tweet-nlp/"

def cmu_tweetnlp_pos(finput):

	with open(finput) as f:
		corpora = f.readlines()

	results=[]
	counter=0
	n_lines=len(corpora)

	#tokenize each line, pos-tag it and save in results
	for line in corpora:

		proc = subprocess.Popen([CMU_ARK_DIR+"runTagger.sh",'--output-format','conll','--model',CMU_ARK_DIR+'models/model.ritter_ptb_alldata_fixed.20130723'],stdout=subprocess.PIPE,stdin=subprocess.PIPE)
		proc.stdin.write(line)
		postags=proc.communicate()[0]
		postags=postags.split("\n")

		tagged_sentence=[]
		for p in postags:
			pos=p.split("\t")
			if len(pos)>1:	
				token=pos[0]
				tag=pos[1]
				token_tag=(token,tag)
				tagged_sentence+=[token_tag]

		results+=[tagged_sentence]
		counter+=1
		print "Progress: ",str(counter)+"/"+str(n_lines),str(float(counter/n_lines)*100)+" %"	
		
	
	#save results
	cmu_tweetnlp_pos_results=open("cmu_tweetnlp_pos_output.txt","w")
	for sentence in results:
		for token_pos in sentence:
			cmu_tweetnlp_pos_results.write(token_pos[0]+" "+token_pos[1]+"\n")
		cmu_tweetnlp_pos_results.write("\n")
	cmu_tweetnlp_pos_results.close()

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='CMU TweetNLP POS Task',epilog="POS with CMU TweetNLP.\n Each input file is a collection of sentences.\nEach line has a sentence or a set of sentences")
	parser.add_argument("-i","--input",nargs=1,help="Input filename",required=True)

	args=vars(parser.parse_args())
	finput=args['input'][0]

	if not os.path.isfile(finput): 
		print "File",freference,"not found"
		sys.exit() 

	cmu_tweetnlp_pos(finput)