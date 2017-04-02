#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys

pos_twitter="raw/pos.txt"
twitterfile_opennlp_pos="annotated/twitter.opennlp.pos.annotated"

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

pos_tagged_phrases=get_tagged_phrases(pos_lines)


twitter_opennlp_pos=open(twitterfile_opennlp_pos,"w")

for phrase in pos_tagged_phrases:
	line=""
	for tagged_token in phrase:
		line+=tagged_token[0]+"_"+tagged_token[1]+" "
	twitter_opennlp_pos.write("%s\n" % line)
twitter_opennlp_pos.close()
