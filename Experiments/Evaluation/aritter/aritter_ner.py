#!/usr/bin/env python2
# -*- coding: utf-8 -*

from __future__ import division

import argparse,os,sys,subprocess
import codecs

ARITTER_DIR="../../../Experiments/Tools/aritter-twitter-nlp/"
os.environ['TWITTER_NLP'] = ARITTER_DIR

def cutoff(string, pattern):
		idx = string.find(pattern)
		return string[:idx if idx != -1 else len(string)]

def aritter_ner(finput):

	with codecs.open(finput,"r", "utf-8") as f:
		corpora = f.readlines()

	results=[]
	counter=0
	n_lines=len(corpora)

	#tokenize each line, pos-tag it and save in results
	for line in corpora:
		# proc = subprocess.Popen(["python2",ARITTER_DIR+"python/ner/extractEntities2.py",'--classify','--pos','--chunk'],stdout=subprocess.PIPE,stdin=subprocess.PIPE)
		proc = subprocess.Popen(["python2",ARITTER_DIR+"python/ner/extractEntities2.py",'--classify'],stdout=subprocess.PIPE,stdin=subprocess.PIPE)
		proc.stdin.write(line)
		ner=proc.communicate()[0]
		ner=cutoff(ner,"Average time per tweet")
		ner=ner.split(" ")

		#extract chunks
		for i in xrange(len(ner)):
			print ner[i]
			ner[i]=(ner[i].split("/")[0],ner[i].split("/")[1].rstrip("\n"))

		results+=[ner]
		counter+=1

		aritter_ner_results=codescs.open("aritter_ner_output.txt","a","utf-8")
		for token_ner in ner:
				aritter_ner_results.write(token_ner[0]+" "+token_ner[1]+"\n")
			aritter_ner_results.write("\n")
		aritter_ner_results.close()

		print "Progress: ",str(counter)+"/"+str(n_lines),str(float(counter/n_lines)*100)+" %"	
	

	# aritter_ner_results=open("aritter_ner_output.txt","w")
	# for sentence in results:
	# 	for token_pos in sentence:
	# 		aritter_ner_results.write(token_pos[0]+" "+token_pos[1]+"\n")
	# 	aritter_ner_results.write("\n")
	# aritter_ner_results.close()

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='Aritter NER Task',epilog="NER with Aritter.\n Each input file is a collection of sentences.\nEach line has a sentence or a set of sentences")
	parser.add_argument("-i","--input",nargs=1,help="Input filename",required=True)


	args=vars(parser.parse_args())
	finput=args['input'][0]

	if not os.path.isfile(finput): 
		print "File",freference,"not found"
		sys.exit() 

	aritter_ner(finput)





