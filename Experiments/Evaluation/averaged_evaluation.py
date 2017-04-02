#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import division
from decimal import Decimal
from math import sqrt
import argparse,os,sys


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

def evaluate(freference,fpredicted):

	#counters
	total_correct_tokens = []
	total_correct_tags = []
	total_predicted_tokens = []
	total_reference_tokens = []

	#read tagged tokens
	reference_sentences=read_file_to_list(freference)
	predicted_sentences=read_file_to_list(fpredicted)

	if len(reference_sentences)!=len(predicted_sentences):
		print "Warning: Files have different number of sentences"
		print "\tReference File:",str(len(reference_sentences)),"sentences"
		print "\tPredicted File:",str(len(predicted_sentences)),"sentences"

	n_documents=len(reference_sentences)
	print "Number of documents: ",n_documents
	for i in xrange(len(predicted_sentences)):											#for each sentence
		total_predicted_tokens+=[len(predicted_sentences[i])]
		total_reference_tokens+=[len(reference_sentences[i])]

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

		total_correct_tokens+=[correct_tokens]
		total_correct_tags+=[correct_tags]

	return total_reference_tokens,total_predicted_tokens,total_correct_tags,total_correct_tokens,n_documents

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
		print "File",fpredicted,"not found"
		sys.exit() 

	total_reference_tokens,total_predicted_tokens,total_correct_tags,total_correct_tokens,n_documents=evaluate(freference,fpredicted)

	#compute token p,r,f1 averages
	#Macro-average Method
	avg_token_precision=Decimal()
	avg_token_recall=Decimal()
	avg_token_document=Decimal()
	for i in xrange(len(total_reference_tokens)):
		avg_token_precision+=100*Decimal(total_correct_tokens[i]/total_predicted_tokens[i])
		avg_token_recall+=100*Decimal(total_correct_tokens[i]/total_reference_tokens[i])
		avg_token_document+=Decimal(total_reference_tokens[i]/n_documents)
	avg_token_precision=avg_token_precision/len(total_reference_tokens)
	avg_token_recall=avg_token_recall/len(total_reference_tokens)
	avg_token_f1=Decimal(2*avg_token_precision*avg_token_recall/(avg_token_precision+avg_token_recall))

	#compute token p,r,f1 std deviations
	#http://www.inorganicventures.com/accuracy-precision-mean-and-standard-deviation
	token_precision_std_dev=Decimal()
	token_recall_std_dev=Decimal()
	token_f1_std_dev=Decimal()
	for i in xrange(len(total_reference_tokens)):
		token_precision_i=100*Decimal(total_correct_tokens[i]/total_predicted_tokens[i])
		token_recall_i=100*Decimal(total_correct_tokens[i]/total_reference_tokens[i])
		try:
			token_f1_i=Decimal(2*token_precision_i*token_recall_i/(token_precision_i+token_recall_i))
		except:
			token_f1_i=100

		token_precision_std_dev+=(token_precision_i-avg_token_precision)**2
		token_recall_std_dev+=(token_recall_i-avg_token_recall)**2
		token_f1_std_dev+=(token_f1_i-avg_token_f1)**2
	token_precision_std_dev=sqrt(token_precision_std_dev/(len(total_reference_tokens)-1))
	token_recall_std_dev=sqrt(token_recall_std_dev/(len(total_reference_tokens)-1))
	token_f1_std_dev=sqrt(token_f1_std_dev/(len(total_reference_tokens)-1))

	print "#####Tokenization Results:#####"
	print "Total Tokens: ",format(sum(total_reference_tokens),'.0f')
	print "Average Token per Document: ",format(avg_token_document,'.0f')
	print "Average Token Precision: ",format(avg_token_precision,'.2f')+"%","+/-",format(token_precision_std_dev,'.2f')
	print "Average Token Recall: ",format(avg_token_recall,'.2f')+"%","+/-",format(token_recall_std_dev,'.2f')
	print "Average Token F1 score: ",format(avg_token_f1,'.2f')+"%","+/-",format(token_f1_std_dev,'.2f')

	#compute tag p,r,f1 averages
	avg_tag_precision=Decimal()
	avg_tag_recall=Decimal()
	for i in xrange(len(total_reference_tokens)):
		avg_tag_precision+=100*Decimal(total_correct_tags[i]/total_predicted_tokens[i])
		avg_tag_recall+=100*Decimal(total_correct_tags[i]/total_reference_tokens[i])

	avg_tag_precision=avg_tag_precision/len(total_reference_tokens)
	avg_tag_recall=avg_tag_recall/len(total_reference_tokens)
	avg_tag_f1=Decimal(2*avg_tag_precision*avg_tag_recall/(avg_tag_precision+avg_tag_recall))

	#compute tag p,r,f1 std deviations
	tag_precision_std_dev=Decimal()
	tag_recall_std_dev=Decimal()
	tag_f1_std_dev=Decimal()
	for i in xrange(len(total_reference_tokens)):
		tag_precision_i=100*Decimal(total_correct_tags[i]/total_predicted_tokens[i])
		tag_recall_i=100*Decimal(total_correct_tags[i]/total_reference_tokens[i])
		try:
			tag_f1_i=Decimal(2*tag_precision_i*tag_recall_i/(tag_precision_i+tag_recall_i))
		except:
			tag_f1_i=100

		tag_precision_std_dev+=(tag_precision_i-avg_tag_precision)**2
		tag_recall_std_dev+=(tag_recall_i-avg_tag_recall)**2
		tag_f1_std_dev+=(tag_f1_i-avg_tag_f1)**2
	tag_precision_std_dev=sqrt(tag_precision_std_dev/(len(total_reference_tokens)-1))
	tag_recall_std_dev=sqrt(tag_recall_std_dev/(len(total_reference_tokens)-1))
	tag_f1_std_dev=sqrt(tag_f1_std_dev/(len(total_reference_tokens)-1))


	print "\n#####Tagging Results:#####"
	print "Average Tag Precision: ",format(avg_tag_precision,'.2f')+"%","+/-",format(tag_precision_std_dev,'.2f')
	print "Average Tag Recall: ",format(avg_tag_recall,'.2f')+"%","+/-",format(tag_recall_std_dev,'.2f')
	print "Average Tag F1 score: ",format(avg_tag_f1,'.2f')+"%","+/-",format(tag_f1_std_dev,'.2f')





