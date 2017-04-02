#!/usr/bin/env python2
# -*- coding: utf-8 -*-

def read_file_to_list(filename):

	with open(filename) as f:
		lines = f.readlines()

	tagged_sentences=[]
	sentence=[]
	for line in lines:
		# if line!='\n' and line!=' \n':
		if line!='\n':
			sentence+=[(line.split(" ")[0],line.split(" ")[1].rstrip("\n"))]
		else:
			tagged_sentences+=[sentence]
			sentence=[]

	return tagged_sentences

def convert_chunk_to_reuters(filename):

	with open(filename) as f:
		lines = f.readlines()


	nltk_chunk_ready=open("aritter_chunk_output_ready.txt","w")
	for line in lines:
		if line!="\n":
			l=line.split(" ")
			nltk_chunk_ready.write(l[0]+" "+l[1].upper().rstrip("\n")+"\n")
		else:
			nltk_chunk_ready.write("\n")
	nltk_chunk_ready.close()

def convert_ner_to_reuters(filename):

	with open(filename) as f:
		lines = f.readlines()


	nltk_chunk_ready=open("aritter_ner_output_ready.txt","w")
	for line in lines:
		if line!="\n":
			l=line.split(" ")
			iob_ent=l[1].rstrip("\n")
			if "-" in l[1]:
				iob=iob_ent.split("-")[0]
				ent=iob_ent.split("-")[1]

				if ent=="geo":
					ent="LOC"
				if ent=="person":
					ent="PER"
				if ent=="company" or ent=="facility" or ent=="product" or ent=="band" or ent=="sportsteam":
					ent="ORG"
				if ent=="other" or ent=="movie" or ent=="tvshow":
					ent="MISC"

				iob_ent=iob+"-"+ent.upper()
			nltk_chunk_ready.write(l[0]+" "+iob_ent+"\n")
		else:
			nltk_chunk_ready.write("\n")
	nltk_chunk_ready.close()


def normalize(freference,fpredicted):

	for i in xrange(len(freference)):
		if freference[i][0][0]!=fpredicted[i][0][0]:
			fpredicted[i]+=fre



if __name__ == '__main__':
	# fname="aritter_chunk_output.txt"
	# convert_chunk_to_reuters(fname)

	# fname="aritter_ner_output.txt"
	# convert_ner_to_reuters(fname)