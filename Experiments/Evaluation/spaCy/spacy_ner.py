#!/usr/bin/env python2
# -*- coding: utf-8 -*

from __future__ import division

import argparse,os,sys
from spacy.en import English
from StringIO import StringIO

reload(sys)
sys.setdefaultencoding("utf-8")

def spacy_ner(finput):

	with open(finput) as f:
		corpora = f.readlines()

	results=[]
	counter=0
	n_lines=len(corpora)

	nlp = English()

	#tokenize each line, ner-tag it and save in results
	for line in corpora:

		#process document
		doc = nlp(unicode(line.rstrip("\n"), "utf-8"))
		
		ner=[]
		last_type=''
		for i in xrange(len(doc)):
			iob=str(doc[i].ent_iob_)
			if iob=='B':
				last_type=str(doc[i].ent_type_)

				if last_type=='PERSON':
					last_type='PER'
				elif last_type=='NORP' or last_type=='EVENT' or last_type=='WORK_OF_ART' or last_type=='LAW' or last_type=='LANGUAGE' or last_type=='DATE' or last_type=='TIME' or last_type=='PERCENT' or last_type=='MONEY' or last_type=='QUANTITY' or last_type=='ORDINAL' or last_type=='CARDINAL':
					last_type='MISC'
				elif last_type=='FACILITY' or last_type=='GPE':
					last_type='LOC'
				elif last_type=='PRODUCT':
					last_type='ORG'

			if iob!='O':
				ner+=[(str(doc[i].text),last_type)]
			else:
				ner+=[(str(doc[i].text),'O')]

		results+=[ner]
		counter+=1
		print "Progress: ",str(counter)+"/"+str(n_lines),str(float(counter/n_lines)*100)+" %"	
	

	spacy_ner_results=open("spacy_ner_output.txt","w")
	for sentence in results:
		for token_ner in sentence:
			spacy_ner_results.write(token_ner[0]+" "+token_ner[1]+"\n")
		spacy_ner_results.write("\n")
	spacy_ner_results.close()

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='SPACY POS Task',epilog="POS with SPACY.\n Each input file is a collection of sentences.\nEach line has a sentence or a set of sentences")
	parser.add_argument("-i","--input",nargs=1,help="Input filename",required=True)


	args=vars(parser.parse_args())
	finput=args['input'][0]

	if not os.path.isfile(finput): 
		print "File",finput,"not found"
		sys.exit() 

	spacy_ner(finput)





