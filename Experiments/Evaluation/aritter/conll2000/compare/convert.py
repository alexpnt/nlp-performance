#!/usr/bin/env python2
# -*- coding: utf-8 -*

from __future__ import division

import argparse,os,sys,subprocess
import codecs

def convert2conll(finput):

	with codecs.open(finput,"r", "utf-8") as f:
		corpora = f.readlines()

	#tokenize each line, chunk-tag it and save in results
	for line in corpora:
		chunk=line.split(" ")
		#extract named ents
		for i in xrange(len(chunk)):
			# print chunk[i]
			chunk[i]=(chunk[i].split("/")[0],chunk[i].split("/")[3].rstrip("\n"))

		aritter_chunk_results=codecs.open("aritter_conll2000.iob.chunk","a","utf-8")
		for token_chunk in chunk:
			aritter_chunk_results.write(token_chunk[0]+" "+token_chunk[1]+"\n")
		aritter_chunk_results.write("\n")
	aritter_chunk_results.close()


if __name__ == '__main__':

	finput="aritter_conll2000.chunk"
	convert2conll(finput)





