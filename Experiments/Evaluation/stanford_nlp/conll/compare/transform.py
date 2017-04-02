#!/usr/bin/env python2
# -*- coding: utf-8 -*-

def convert_ner_to_aritter(filename):

	with open(filename) as f:
		lines = f.readlines()


	nltk_ner_ready=open("nltk_ner_output_ready.txt","w")
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
			nltk_ner_ready.write(l[0]+" "+iob_ent+"\n")
		else:
			nltk_ner_ready.write("\n")
	nltk_ner_ready.close()


if __name__ == '__main__':
	# fname="nltk_chunk_output.txt"
	# convert_nltk_chunk_to_aritter(fname)

	fname="stanford_nlp_ner_output.txt"
	convert_ner_to_aritter(fname)
