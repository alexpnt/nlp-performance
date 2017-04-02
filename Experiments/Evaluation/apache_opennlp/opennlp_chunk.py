#!/usr/bin/env python2
# -*- coding: utf-8 -*

import subprocess,os,argparse
from StringIO import StringIO
import sys

OPENNLP_DIR="../../../Experiments/Tools/apache-opennlp-1.6.0/"

def opennlp_chunk(finput):

	with open(finput) as f:
		corpora = f.readlines()

	results=[]
	counter=0
	n_lines=len(corpora)

	#tokenize each line, pos-tag it and chunk
	for line in corpora:
		proc = subprocess.Popen([OPENNLP_DIR+"bin/opennlp",'POSTagger',OPENNLP_DIR+'models/en-pos-maxent.bin'],stdout=subprocess.PIPE,stdin=subprocess.PIPE)
		proc.stdin.write(line)
		pos=proc.communicate()[0]

		proc = subprocess.Popen([OPENNLP_DIR+"bin/opennlp",'ChunkerME',OPENNLP_DIR+'models/en-iobchunker.bin'],stdout=subprocess.PIPE,stdin=subprocess.PIPE)
		proc.stdin.write(pos)
		chunks=proc.communicate()[0].strip()
		chunks=chunks.replace("[","[ ")
		chunks=chunks.split(" ")
		# print chunks
		chunked_sentence=[]
		chunk_flag=False
		iterable = iter(xrange(len(chunks)))
		for i in iterable:							#iterate over the POS tagged words
			# print chunks[i]
			if chunks[i]=='[' and i+2<len(chunks) and (chunks[i+1]=="NP" or chunks[i+1]=="VP" or chunks[i+1]=="PP"):	#starting of a chunk (B-)
				chunk_flag=True
				b_chunk="B-"+chunks[i+1]
				chunked_sentence+=[(chunks[i+2].split("_")[0],b_chunk)]
				[iterable.next() for x in range(2)]
				continue
			elif chunks[i]==']':					#ending of a chunk
				chunk_flag=False
				continue

			if chunk_flag:							#inside of a chunk (I-)
				try:
					i_chunk="I-"+chunks[i].split("_")[1]
					chunked_sentence+=[(chunks[i].split("_")[0],i_chunk)]
				except Exception, e:
					print i
					print chunks
					print chunks[i]
					raise e
			elif not chunk_flag:									#outside of a chunk (O-)
				chunked_sentence+=[(chunks[i].split("_")[0],'O')]

		# print
		# print chunked_sentence
		results+=[chunked_sentence]
		counter+=1
		print "Progress: ",str(counter)+"/"+str(n_lines),str(float(counter/n_lines)*100)+" %"	
		
	
	#save in results
	opennlp_chunk_results=open("opennlp_chunk_output.txt","w")
	for chunked_sentence in results:
		for token_chunk in chunked_sentence:
			if token_chunk[0]!='' and token_chunk[0]!='SBAR':
				opennlp_chunk_results.write(token_chunk[0]+" "+token_chunk[1]+"\n")
		opennlp_chunk_results.write("\n")
	opennlp_chunk_results.close()

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='OPENNLP Chunking Task',epilog="Chwunk with OPENNLP.\n Each input file is a collection of sentences.\nEach line has a sentence or a set of sentences")
	parser.add_argument("-i","--input",nargs=1,help="Input filename",required=True)


	args=vars(parser.parse_args())
	finput=args['input'][0]

	if not os.path.isfile(finput): 
		print "File",freference,"not found"
		sys.exit() 

	opennlp_chunk(finput)
