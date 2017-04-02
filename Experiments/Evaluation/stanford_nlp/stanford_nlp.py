#!/usr/bin/env python2
# -*- coding: utf-8 -*

import subprocess,os,argparse
from StringIO import StringIO
import sys
from nltk.internals import find_jars_within_path
from nltk.tag import StanfordPOSTagger
from nltk.tokenize import StanfordTokenizer


STANDORD_NLP="../../../Experiments/Tools/CoreNLP/lib/"
os.environ["CLASSPATH"] = "../../../Experiments/Evaluation/stanford_nlp/lib/stanford-postagger-full-2015-12-09/stanford-postagger.jar"
os.environ["STANFORD_MODELS"]="../../../Experiments/Evaluation/stanford_nlp/lib/stanford-postagger-full-2015-12-09/models"
def stanford_nlp_pos(finput):

	with open(finput) as f:
		corpora = f.readlines()

	results=[]
	counter=0
	n_lines=len(corpora)

	#tokenize each line, pos-tag it and save in results
	st = StanfordPOSTagger('english-bidirectional-distsim.tagger') 
	stanford_dir = st._stanford_jar.rpartition('/')[0]
	stanford_jars = find_jars_within_path(stanford_dir)
	st._stanford_jar = ':'.join(stanford_jars)
	for line in corpora:
		# tokens = StanfordTokenizer('english-bidirectional-distsim.tagger').tokenize(line)	
		st.tag(line.split())
		return

	# 	pos=st.tag(tokens)
	# 	results+=[pos]
	# 	counter+=1

	# 	print "Progress: ",str(counter)+"/"+str(n_lines),str(float(counter/n_lines)*100)+" %"	
		
	
	# #save results
	# cmu_tweetnlp_pos_results=open("stanford_nlp_pos_output.txt","w")
	# for sentence in results:
	# 	for token_pos in sentence:
	# 		cmu_tweetnlp_pos_results.write(token_pos[0]+" "+token_pos[1]+"\n")
	# 	cmu_tweetnlp_pos_results.write("\n")
	# cmu_tweetnlp_pos_results.close()

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='STANDORD NLP POS Task',epilog="POS with STANDORD NLP.\n Each input file is a collection of sentences.\nEach line has a sentence or a set of sentences")
	parser.add_argument("-i","--input",nargs=1,help="Input filename",required=True)

	args=vars(parser.parse_args())
	finput=args['input'][0]

	if not os.path.isfile(finput): 
		print "File",freference,"not found"
		sys.exit() 

	stanford_nlp_pos(finput)