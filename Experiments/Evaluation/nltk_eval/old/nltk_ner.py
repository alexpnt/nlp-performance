from __future__ import division
from decimal import Decimal
from nltk import word_tokenize,pos_tag,ne_chunk,data
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams
from nltk.chunk import tree2conlltags

DATASETS_DIR="/home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/dados/Twitter/"
twitter_annotaded_ner=DATASETS_DIR+"Aritter/annotaded/ner.txt"
twitter_corpora=DATASETS_DIR+"Aritter/raw/arriter_tweet_ner_corpora.txt"

def get_nltk_ner_twitter(percentage=1.0):

	with open(twitter_corpora) as f:
		corpora = f.readlines()

	results=[]
	n_tweets=len(corpora)
	n_tweets=int(n_tweets*percentage)
	counter=0

	#tokenize each tweet, pos-tag it, ner tag it and save in results
	for i in xrange(0,n_tweets):
		tokens = word_tokenize(corpora[i])	
		pos=pos_tag(tokens)

		# Loads the serialized NEChunkParser object
		chunker = data.load('chunkers/maxent_ne_chunker/english_ace_multiclass.pickle')
		maxEnt_classifier = chunker._tagger.classifier()
		maxEnt_labels=maxEnt_classifier.labels()
		ner=tree2conlltags(ne_chunk(pos,binary=False))
		
		results+=[ner]
		counter+=1
		print "Progress: ",str(counter)+"/"+str(n_tweets),str(float(counter/n_tweets)*100)+" %"	
	

	# for tweet in results:
	# 	print tweet
	nltk_ner_twitter=open("nltk_ner_twitter.txt","w")
	for tweet_ner in results:
		for token_ner in tweet_ner:
			nltk_ner_twitter.write(token_ner[0]+" "+token_ner[2]+"\n")
		nltk_ner_twitter.write("\n")
	nltk_ner_twitter.close()
	return results

def get_twitter_annotated_ner(n_tweets):

	with open(twitter_annotaded_ner) as f:
		twitter_ner_tags = f.readlines()

	twitter_ner_results=[]
	token_ner=[]
	counter=0
	for t in twitter_ner_tags:
		if counter==n_tweets:
			break
		if t!=' \n':
			token_ner+=[[t.split(" ")[0],t.split(" ")[1].rstrip('\n')]]
		else:
			twitter_ner_results+=[token_ner]
			token_ner=[]
			counter+=1

	# for tweet in twitter_ner_results:
	# 	print tweet
	return twitter_ner_results

def get_ner_evaluation(nltk_anottated_tweets,annotated_tweets):


	correct_tags=found_guessed=total_tokens=unmatched=0

	#for each tweet annotated by nltk
	for i in xrange(0,len(nltk_anottated_tweets)):
		token_alignment={}

		#match tokens
		last_found_index=0
		nltk_token_index=0

		#for each token in the tweet
		for nltk_token in nltk_anottated_tweets[i]:
			found=False
			for j in xrange(last_found_index,len(annotated_tweets[i])):		#search for respective equal token
				if nltk_token[0]==annotated_tweets[i][j][0]:
					found=True
					last_found_index=j
					token_alignment[nltk_token_index]=j						#save matching, if found
			if not found:
				token_alignment[nltk_token_index]=None
			nltk_token_index+=1


		#debug
		#nltk_twitter_token,nltk_twitter_ner <=> aritter_twitter_token,aritter_twitter_ner
		
		# for nltk_token_index in token_alignment:
		# 	if token_alignment[nltk_token_index] is not None:
		# 		print nltk_anottated_tweets[i][nltk_token_index][0],nltk_anottated_tweets[i][nltk_token_index][2]+" <=> "+annotated_tweets[i][token_alignment[nltk_token_index]][0],annotated_tweets[i][token_alignment[nltk_token_index]][1]
		
		#statistics
		for nltk_token_index in token_alignment:
			if token_alignment[nltk_token_index] is not None:
				expected_tag=annotated_tweets[i][token_alignment[nltk_token_index]][1]
				predicted_tag=nltk_anottated_tweets[i][nltk_token_index][2]
				
				if '-' in predicted_tag:
					predicted_iob=predicted_tag.split("-")[0]
					predicted_entity=predicted_tag.split("-")[1]
					predicted_tag=predicted_iob+"-"+predicted_entity.lower()


				if expected_tag==predicted_tag:
					correct_tags+=1
				found_guessed+=1
			else:
				unmatched+=1
			total_tokens+=1

	return correct_tags,found_guessed,total_tokens,unmatched

if __name__ == '__main__':

	nltk_ner=get_nltk_ner_twitter(0.001)
	twitter_ner=get_twitter_annotated_ner(len(nltk_ner))

	results=get_ner_evaluation(nltk_ner,twitter_ner)

	print "\n#####Results:#####"
	precision=100*Decimal(results[0]/results[1])
	recall=100*Decimal(results[0]/results[2])
	f1=Decimal(2*precision*recall/(precision+recall))
	print "Precision: ",format(precision,'.2f')+"%"
	print "Recall: ",format(recall,'.2f')+"%"
	print "F1 score: ",format(f1,'.2f')+"%"





