from __future__ import division
from decimal import Decimal
from nltk import word_tokenize,pos_tag,ne_chunk,data
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams

DATASETS_DIR="/home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/dados/Conll/"
conll_annotaded_pos=DATASETS_DIR+"reuters.annotated"
conll_corpora=DATASETS_DIR+"reuters.raw"

# def get_nltk_pos_reuters():

# 	with open(conll_corpora) as f:
# 		corpora = f.readlines()

# 	tokens = word_tokenize(corpora[0])	
# 	pos_tags=pos_tag(tokens)	

# 	nltk_pos_reuters=open("nltk_pos_reuters.txt","w")
# 	for token_pos in pos_tags:
# 		nltk_pos_reuters.write(token_pos[0]+" "+token_pos[1]+"\n")
# 	nltk_pos_reuters.close()get_nltk_pos_reuters

# 	return pos_tags

def get_reuters_tokenization():
	with open(conll_annotaded_pos) as f:
		reuters_tags = f.readlines()

	reuters_tokens=[]
	for t in reuters_tags:
		reuters_tokens+=[t.split(" ")[0]]

	return reuters_tokens


def get_reuters_annotated_pos():

	with open(conll_annotaded_pos) as f:
		reuters_pos_tags = f.readlines()

	reuters_pos_results=[]
	token_pos=[]
	for t in reuters_pos_tags:
			token_pos=(t.split(" ")[0],t.split(" ")[1])
			reuters_pos_results+=[token_pos]

	return reuters_pos_results

def get_reuters_nltk_annotated_pos():

	reuter_tokens=get_reuters_tokenization()
	reuters_nltk_pos_results=pos_tag(reuter_tokens)	

	return reuters_nltk_pos_results

def get_pos_evaluation(nltk_anottated_reuters,annotated_reuters):


	correct_tags=found_guessed=total_tokens=0

	for i in xrange(len(annotated_reuters)):
		if annotated_reuters[i][1]==nltk_anottated_reuters[i][1]:
			correct_tags+=1
		found_guessed+=1

	# token_al	ignment={}

	# #match tokens
	# last_found_index=0
	# nltk_token_index=0

	# already_selected=[]
	# #for each token in the corpora
	# for nltk_token in nltk_anottated_reuters:
	# 	found=False
	# 	for j in xrange(last_found_index,len(annotated_reuters)):		#search for respective equal token
	# 		if nltk_token[0]==annotated_reuters[j][0]:
	# 			found=True
	# 			if j not in already_selected:
	# 				last_found_index=j
	# 				already_selected+=[j]
	# 				token_alignment[nltk_token_index]=j						#save matching, if found
	# 				break
	# 			else:
	# 				continue
	# 	if not found:
	# 		token_alignment[nltk_token_index]=None
	# 		last_found_index=0

	# 	nltk_token_index+=1



	#debug
	#nltk_reuters_token,nltk_reuters_pos <=> reuters_token,reuters_pos 
	
	# for nltk_token_index in token_alignment:
	# 	if token_alignment[nltk_token_index] is not None:
	# 		print nltk_anottated_reuters[nltk_token_index][0],nltk_anottated_reuters[nltk_token_index][1]+" <=> "+annotated_reuters[token_alignment[nltk_token_index]][0],annotated_reuters[token_alignment[nltk_token_index]][1]
	

	#statistics
	# for nltk_token_index in token_alignment:
	# 	if token_alignment[nltk_token_index] is not None:
	# 		if nltk_anottated_reuters[nltk_token_index][1]==annotated_reuters[token_alignment[nltk_token_index]][1]:
	# 			correct_tags+=1
	# 		found_guessed+=1
	# 	total_tokens+=1
	# 	
	# 	
	# 	

	return correct_tags,found_guessed,total_tokens

if __name__ == '__main__':


	reuter_pos=get_reuters_annotated_pos()
	nltk_reuters_pos=get_reuters_nltk_annotated_pos()
	results=get_pos_evaluation(nltk_reuters_pos,reuter_pos)

	print "\n#####Results:#####"
	precision=100*Decimal(results[0]/results[1])
	print "Precision: ",format(precision,'.2f')+"%"


	# print "POS Tagging ..."
	# nltk_reuters_pos=get_nltk_pos_reuters()
	# print "Reading expected annotations ..."
	# reuters_pos=get_reuters_annotated_pos()

	# print "Evaluating ..."
	# results=get_pos_evaluation(nltk_reuters_pos,reuters_pos)

	# print "\n#####Results:#####"
	# precision=100*Decimal(results[0]/results[1])
	# recall=100*Decimal(results[0]/results[2])
	# f1=Decimal(2*precision*recall/(precision+recall))
	# print "Precision: ",format(precision,'.2f')+"%"
	# print "Recall: ",format(recall,'.2f')+"%"
	# print "F1 score: ",format(f1,'.2f')+"%"





