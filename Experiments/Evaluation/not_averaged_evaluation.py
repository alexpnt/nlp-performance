#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import division
from decimal import Decimal
import argparse,os,sys


def read_file_to_list(filename):

	with open(filename) as f:
		lines = f.readlines()

	tagged_sentences=[]
	sentence=[]
	for line in lines:
		if line!='\n' and line!=' \n':
			sentence+=[(line.split(" ")[0],line.split(" ")[1].rstrip("\n"))]
		else:
			tagged_sentences+=[sentence]
			sentence=[]

	return tagged_sentences

def evaluate(freference,fpredicted):

	#counters
	total_correct_tokens = 0
	total_correct_tags = 0
	total_predicted_tokens = 0
	total_reference_tokens = 0

	#read tagged tokens
	reference_sentences=read_file_to_list(freference)
	predicted_sentences=read_file_to_list(fpredicted)

	if len(reference_sentences)!=len(predicted_sentences):
		print "Warning: Files have different number of sentences"
		print "\tReference File:",str(len(reference_sentences)),"sentences"
		print "\tPredicted File:",str(len(predicted_sentences)),"sentences"

	print "Number of documents: ",len(reference_sentences)
	for i in xrange(len(predicted_sentences)):											#for each sentence
		total_predicted_tokens+=len(predicted_sentences[i])
		total_reference_tokens+=len(reference_sentences[i])

		correct_tokens=correct_tags=index_p=index_r=0
		while predicted_sentences[i] and reference_sentences[i]:
			if predicted_sentences[i][0][0] == reference_sentences[i][0][0]:  			# correct token
				correct_tokens += 1
				if predicted_sentences[i][0][1] == reference_sentences[i][0][1]: 		# correct tag 
					correct_tags += 1
				index_p += len(predicted_sentences[i][0][0]) 							# move to the next token
				index_r += len(reference_sentences[i][0][0])							# move to the next token
				predicted_sentences[i].pop(0)
				reference_sentences[i].pop(0)
			else:
				if index_p == index_r:
					index_p += len(predicted_sentences[i][0][0]) 						# move to the next token
					index_r += len(reference_sentences[i][0][0])						# move to the next token
					predicted_sentences[i].pop(0)
					reference_sentences[i].pop(0)
				elif index_p < index_r:
					index_p += len(predicted_sentences[i][0][0])
					predicted_sentences[i].pop(0)
				elif index_p > index_r:
					index_r += len(reference_sentences[i][0][0]) 						# move to the next token
					reference_sentences[i].pop(0)

		total_correct_tokens+=correct_tokens
		total_correct_tags+=correct_tags

	return total_reference_tokens,total_predicted_tokens,total_correct_tags,total_correct_tokens

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='NLP Evaluation',epilog="Evaluation Program for generic NLP tasks.\n Each file is a collection of tagged sentences.\nEach line has a word and a tag separated by space and each phrase is separated by an empty line.")
	parser.add_argument("-r","--reference",nargs=1,help="Reference filename",required=True)
	parser.add_argument("-p","--predicted",nargs=1,help="Predicted filename",required=True)


	args=vars(parser.parse_args())
	freference=args['reference'][0]
	fpredicted=args['predicted'][0]

	if not os.path.isfile(freference): 
		print "File",freference,"not found"
		sys.exit() 
	if not os.path.isfile(fpredicted): 
		print "File",freference,"not found"
		sys.exit() 

	total_reference_tokens,total_predicted_tokens,total_correct_tags,total_correct_tokens=evaluate(freference,fpredicted)

	print "Total tokens: ",total_reference_tokens
	print "#####Tokenization Results:#####"
	token_precision=100*Decimal(total_correct_tokens/total_predicted_tokens)
	token_recall=100*Decimal(total_correct_tokens/total_reference_tokens)
	token_f1=Decimal(2*token_precision*token_recall/(token_precision+token_recall))
	print "Token Precision: ",format(token_precision,'.2f')+"%"
	print "Token Recall: ",format(token_recall,'.2f')+"%"
	print "Token F1 score: ",format(token_f1,'.2f')+"%"

	print "\n#####Tagging Results:#####"
	tag_precision=100*Decimal(total_correct_tags/total_predicted_tokens)
	tag_recall=100*Decimal(total_correct_tags/total_reference_tokens)
	tag_f1=Decimal(2*tag_precision*tag_recall/(tag_precision+tag_recall))
	print "Tag Precision: ",format(tag_precision,'.2f')+"%"
	print "Tag Recall: ",format(tag_recall,'.2f')+"%"
	print "Tag F1 score: ",format(tag_f1,'.2f')+"%"





