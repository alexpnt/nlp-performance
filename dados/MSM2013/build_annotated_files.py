#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import search_sequence

def write_annotated_files(ents_file,tweets_file):

	ner_filename="msm2013.ner"

	#read
	with open(tweets_file) as f:
		tweets = f.read().splitlines()

	with open(ents_file) as f:
		ents = f.read().splitlines()

	#build lists of lists with annotated entities for each tweet
	entities=[]
	for ent in ents:
		spl=ent.split(";")
		tweet_entities=[]
		for i in xrange(len(spl)-1):
			tweet_entities+=[(spl[i].split("/")[0],spl[i].split("/")[1])]
		entities+=[tweet_entities]

	fner=open(ner_filename,"w")
	for i in xrange(len(tweets)):						#iterate over tweets
		tweet_tokenized=tweets[i].split(" ")
		ent_indexes=[]
		if len(entities[i])!=0:
			# print entities[i]
			for ent in entities[i]:						#for each detected entity
				ent_index=search_sequence.search(tweet_tokenized,ent[1].split(" "))		#search the entity in the original tweet (get the index)
				ent_indexes+=[(ent_index,len(ent[1].split(" ")))]						#save the index and the len of the entity (n words)
			# print ent_indexes
		

		annotations=['O']*len(tweet_tokenized)											#initialize named entities
		for j in xrange(len(ent_indexes)):												#for each index found
			for z in xrange(ent_indexes[j][1]):											#for each repetion (when a named entity is more thanone word)
				annotations[ent_indexes[j][0]+z]=entities[i][j][0]						#assign entity to token
		

		
		#write to file the tokens and named entities
		for w in xrange(len(tweet_tokenized)):
			fner.write("%s %s\n" % (tweet_tokenized[w],annotations[w]))
		fner.write("\n")

	fner.close()

if __name__ == '__main__':
	ents_file="entities.txt"
	tweets_file="tweets.txt"
	write_annotated_files(ents_file,tweets_file)




	