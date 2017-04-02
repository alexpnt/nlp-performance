#!/usr/bin/env python2
# -*- coding: utf-8 -*-

def convert_spacy_chunk_to_aritter(filename):

	with open(filename) as f:
		lines = f.readlines()


	spacy_chunk_ready=open("spacy_chunk_output_ready.txt","w")
	for line in lines:
		if line!="\n":
			l=line.split(" ")
			spacy_chunk_ready.write(l[0]+" "+l[1].lower().rstrip("\n")+"\n")
		else:
			spacy_chunk_ready.write("\n")
	spacy_chunk_ready.close()

def convert_spacy_ner_to_aritter(filename):

	with open(filename) as f:
		lines = f.readlines()


	spacy_chunk_ready=open("spacy_ner_output_ready.txt","w")
	for line in lines:
		if line!="\n":
			l=line.split(" ")
			iob_ent=l[1].rstrip("\n")
			if "-" in l[1]:
				iob=iob_ent.split("-")[0]
				ent=iob_ent.split("-")[1].lower()

				if ent=="gpe" or ent=="gsp" or ent=="location":
					ent="geo-loc"
				iob_ent=iob+"-"+ent
			spacy_chunk_ready.write(l[0]+" "+iob_ent+"\n")
		else:
			spacy_chunk_ready.write("\n")
	spacy_chunk_ready.close()


if __name__ == '__main__':
	fname="spacy_chunk_output.txt"
	convert_spacy_chunk_to_aritter(fname)