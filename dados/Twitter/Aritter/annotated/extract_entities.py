#!/usr/bin/env python2
# -*- coding: utf-8 -*-

def extract_entities(filename):

	with open(filename) as f:
		lines = f.readlines()


	nltk_ner_ready=open("aritter_ent_extracted.txt","w")
	lock=0
	for line in lines:
		if line!="\n" and line!=" \n":
			l=line.split(" ")
			iob_ent=l[1].rstrip("\n")
			if "-" in l[1]:
				iob=iob_ent.split("-")[0]
				ent=iob_ent.split("-")[1].upper()

				if ent=="GPE" or ent=="GSP" or ent=="LOCATION":
					ent="GEO-LOC"
				iob_ent=iob+"-"+ent
				nltk_ner_ready.write(l[0]+" "+ent+"\n")
				lock=1
		else:
			if lock==1:
				nltk_ner_ready.write("\n")
				lock=0
	nltk_ner_ready.close()


if __name__ == '__main__':

	fname="ner.txt"
	extract_entities(fname)
