#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys

pos_twitter="raw/pos.txt"
chunk_twitter="raw/chunk.txt"
twitter_pos_chunk="annotated/twitter.pos.chunk.annotated"

def get_tagged_phrases(lines):

	tagged_phrases=[]
	phrase=[]
	for i in xrange(len(lines)):
		if lines[i]!='\n':
			token=lines[i].split(" ")[0]
			tag=lines[i].split(" ")[1].strip("\n")
			phrase+=[(token,tag)]
		else:
			tagged_phrases+=[phrase]
			phrase=[]

	return tagged_phrases


with open(pos_twitter) as f:
    pos_lines = f.readlines()

with open(chunk_twitter) as f:
    chunk_lines = f.readlines()


pos_tagged_phrases=get_tagged_phrases(pos_lines)
chunk_tagged_phrases=get_tagged_phrases(chunk_lines)


#The goal is to find and delete non-matching phrases
i=0
# print "SIZE: ",len(chunk_tagged_phrases),len(pos_tagged_phrases)
while len(chunk_tagged_phrases)!=len(pos_tagged_phrases):
	# print i,len(chunk_tagged_phrases[i]),len(pos_tagged_phrases[i])
	if len(chunk_tagged_phrases[i])!=len(pos_tagged_phrases[i]):
		# print "DEL: ",len(chunk_tagged_phrases[i]),len(pos_tagged_phrases[i])
		# print "SIZE: ",len(chunk_tagged_phrases),len(pos_tagged_phrases)
		del chunk_tagged_phrases[i]

	else:
		# print "OKAY:",len(chunk_tagged_phrases[i]),len(pos_tagged_phrases[i])
		i+=1



twitter_pos_chunk_annotated=open(twitter_pos_chunk,"w")

for i in xrange(len(chunk_tagged_phrases)):
	for j in xrange(len(chunk_tagged_phrases[i])):
		line="".join(pos_tagged_phrases[i][j][0]+" "+pos_tagged_phrases[i][j][1]+" "+chunk_tagged_phrases[i][j][1].upper()+"\n")
		twitter_pos_chunk_annotated.write("%s" % line)
	twitter_pos_chunk_annotated.write("\n")
twitter_pos_chunk_annotated.close()
