#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import division
import argparse,os,sys
import collections


def read_file_to_list(filename):

	with open(filename) as f:
		lines = f.readlines()

	tagged_sentences=[]
	sentence=[]
	for line in lines:
		if line!='\n' and line!=' \n':
		# if line!='\n':
			sentence+=[(line.split(" ")[0],line.split(" ")[1].rstrip("\n"))]
		else:
			tagged_sentences+=[sentence]
			sentence=[]

	return tagged_sentences

def gather_stats(freference):

	#counters
	stats={}

	#read tagged tokens
	reference_sentences=read_file_to_list(freference)
	for sentence in reference_sentences:
		for (token,tag) in sentence:
			if tag in stats:
				stats[tag]+=1
			else:
				stats[tag]=1

	return stats


	print "Number of documents: ",len(reference_sentences)

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='Statistics',epilog="Gather Statistics about an annotated file.\n Each file is a collection of tagged sentences.\nEach line has a word and a tag separated by space and each phrase is separated by an empty line.")
	parser.add_argument("-r","--reference",nargs=1,help="Reference filename",required=True)


	args=vars(parser.parse_args())
	freference=args['reference'][0]

	if not os.path.isfile(freference): 
		print "File",freference,"not found"
		sys.exit() 

	stats=gather_stats(freference)
	ordered_stats = collections.OrderedDict(sorted(stats.items()))

	total=sum(stats.values())
	print "There are",len(stats.keys()),"different tags in this dataset"
	tags_counter=0
	tags_per_counter=0.0
	for tag in ordered_stats.keys():
		# if stats[tag]/total*100 < 1:
		# if stats[tag]/total*100 >= 1:
		tags_counter+=stats[tag]
		tags_per_counter+=stats[tag]/total*100
		print "Tag->",tag,"Counter-> ",stats[tag],"(",str(format(stats[tag]/total*100,'.2f')),"% )" 

	print "Total Tags:",tags_counter,"(",format(tags_per_counter,".2f"),"%)"







