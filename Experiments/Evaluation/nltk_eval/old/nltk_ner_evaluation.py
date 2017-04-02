from __future__ import division
from decimal import Decimal
from nltk import word_tokenize,pos_tag,ne_chunk,data
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams
from nltk.chunk import tree2conlltags

DATASETS_DIR="/home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/dados/Conll/"
conll_annotaded_ner=DATASETS_DIR+"reuters.annotated"
conll_corpora=DATASETS_DIR+"reuters.raw"

# def get_nltk_ner_reuters():

# 	with open(conll_corpora) as f:
# 		corpora = f.readlines()

# 	tokens = word_tokenize(corpora[0])	
# 	ner_tags=ner_tag(tokens)	

# 	nltk_ner_reuters=open("nltk_ner_reuters.txt","w")
# 	for token_ner in ner_tags:
# 		nltk_ner_reuters.write(token_ner[0]+" "+token_ner[1]+"\n")
# 	nltk_ner_reuters.close()get_nltk_ner_reuters

# 	return ner_tags

def get_reuters_tokenization():
	with open(conll_annotaded_ner) as f:
		reuters_tags = f.readlines()

	reuters_tokens=[]
	for t in reuters_tags:
		reuters_tokens+=[t.split(" ")[0]]

	return reuters_tokens


def get_reuters_annotated_ner():

	with open(conll_annotaded_ner) as f:
		reuters_ner_tags = f.readlines()

	reuters_ner_results=[]
	token_ner=[]
	for t in reuters_ner_tags:
			token_ner=(t.split(" ")[0],t.split(" ")[3].rstrip('\n'))
			reuters_ner_results+=[token_ner]

	return reuters_ner_results

def get_reuters_nltk_annotated_ner():

	reuter_tokens=get_reuters_tokenization()
	pos=pos_tag(reuter_tokens)	

	chunker = data.load('chunkers/maxent_ne_chunker/english_ace_multiclass.pickle')
	maxEnt_classifier = chunker._tagger.classifier()
	maxEnt_labels=maxEnt_classifier.labels()
	reuters_nltk_ner_results=tree2conlltags(ne_chunk(pos,binary=False))

	return reuters_nltk_ner_results

def get_ner_evaluation(nltk_anottated_reuters,annotated_reuters):


	correct_tags=found_guessed=total_tokens=0

	for i in xrange(len(annotated_reuters)):
		print annotated_reuters[i][1]+"<=>"+nltk_anottated_reuters[i][2]
		# if annotated_reuters[i][3]==nltk_anottated_reuters[i][2]:
		# 	correct_tags+=1
		# found_guessed+=1

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
	#nltk_reuters_token,nltk_reuters_ner <=> reuters_token,reuters_ner 
	
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


	reuter_ner=get_reuters_annotated_ner()
	nltk_reuters_ner=get_reuters_nltk_annotated_ner()
	results=get_ner_evaluation(nltk_reuters_ner,reuter_ner)

	# print "\n#####Results:#####"
	# precision=100*Decimal(results[0]/results[1])
	# print "Precision: ",format(precision,'.2f')+"%"



