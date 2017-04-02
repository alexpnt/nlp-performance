from __future__ import division
from decimal import Decimal
from nltk import word_tokenize,pos_tag,ne_chunk,data
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams

DATASETS_DIR="/home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/dados/Twitter/"
twitter_annotaded_pos=DATASETS_DIR+"Aritter/annotaded/pos.txt"
twitter_corpora=DATASETS_DIR+"Aritter/raw/arriter_tweet_pos_corpora.txt"

def get_nltk_pos_twitter(percentage=1.0):

	with open(twitter_corpora) as f:
		corpora = f.readlines()

	results=[]
	n_tweets=len(corpora)
	n_tweets=int(n_tweets*percentage)
	counter=0

	#tokenize each tweet and pos-tag it, save in results
	for i in xrange(0,n_tweets):
		tokens = word_tokenize(corpora[i])	
		pos=pos_tag(tokens)
		results+=[pos]
		counter+=1
		print "Progress: ",str(counter)+"/"+str(n_tweets),str(float(counter/n_tweets)*100)+" %"	
	

	# for tweet in results:
	# 	print tweet
	nltk_pos_twitter=open("nltk_pos_twitter.txt","w")
	for tweet_pos in results:
		for token_pos in tweet_pos:
			nltk_pos_twitter.write(token_pos[0]+" "+token_pos[1]+"\n")
		nltk_pos_twitter.write("\n")
	nltk_pos_twitter.close()
	return results

def get_twitter_annotated_pos(n_tweets):

	with open(twitter_annotaded_pos) as f:
		twitter_pos_tags = f.readlines()

	twitter_pos_results=[]
	token_pos=[]
	counter=0
	for t in twitter_pos_tags:
		if counter==n_tweets:
			break
		if t!='\n':
			token_pos+=[[t.split(" ")[0],t.split(" ")[1].rstrip('\n')]]
		else:
			twitter_pos_results+=[token_pos]
			token_pos=[]
			counter+=1

	# for tweet in twitter_pos_results:
	# 	print tweet
	return twitter_pos_results

def get_pos_evaluation(nltk_anottated_tweets,annotated_tweets):


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
		#nltk_twitter_token,nltk_twitter_pos <=> aritter_twitter_token,aritter_twitter_pos 
		
		# for nltk_token_index in token_alignment:
		# 	if token_alignment[nltk_token_index] is not None:
		# 		print nltk_anottated_tweets[i][nltk_token_index][0],nltk_anottated_tweets[i][nltk_token_index][1]+" <=> "+annotated_tweets[i][token_alignment[nltk_token_index]][0],annotated_tweets[i][token_alignment[nltk_token_index]][1]
		

		#statistics
		for nltk_token_index in token_alignment:
			if token_alignment[nltk_token_index] is not None:
				if nltk_anottated_tweets[i][nltk_token_index][1]==annotated_tweets[i][token_alignment[nltk_token_index]][1]:
					correct_tags+=1
				found_guessed+=1
			else:
				unmatched+=1
			total_tokens+=1

	return correct_tags,found_guessed,total_tokens,unmatched

if __name__ == '__main__':

	nltk_pos=get_nltk_pos_twitter(0.005)
	twitter_pos=get_twitter_annotated_pos(len(nltk_pos))

	results=get_pos_evaluation(nltk_pos,twitter_pos)

	print "\n#####Results:#####"
	precision=100*Decimal(results[0]/results[1])
	recall=100*Decimal(results[0]/results[2])
	f1=Decimal(2*precision*recall/(precision+recall))
	print "Precision: ",format(precision,'.2f')+"%"
	print "Recall: ",format(recall,'.2f')+"%"
	print "F1 score: ",format(f1,'.2f')+"%"





