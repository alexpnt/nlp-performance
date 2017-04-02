#!/usr/bin/env python2
# -*- coding: utf-8 -*

from __future__ import division

import argparse,os,sys,subprocess
import codecs

def convert2conll(finput):

	with codecs.open(finput,"r", "utf-8") as f:
		corpora = f.readlines()

	results=[]

	#tokenize each line, ner-tag it and save in results
	for line in corpora:
		ner=line.split(" ")
		#extract named ents
		for i in xrange(len(ner)):
			# print ner[i]
			ner[i]=(ner[i].split("/")[0],ner[i].split("/")[1].rstrip("\n"))

		results+=[ner]

		aritter_ner_results=codecs.open("aritter_ner_output.txt","a","utf-8")
		for token_ner in ner:
			aritter_ner_results.write(token_ner[0]+" "+token_ner[1]+"\n")
		aritter_ner_results.write("\n")
	aritter_ner_results.close()


if __name__ == '__main__':

	finput="tweets.ner"
	convert2conll(finput)





