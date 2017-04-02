##########################
#SPACY TWITTER
##########################
#

#produce twitter pos results 
echo 'producing twitter pos results'
./spacy_pos.py -i ../../../dados/Twitter/Aritter/raw/arriter_tweet_pos_corpora.txt

#produce twitter chunking results 
echo 'producing twitter chunking results'
./spacy_chunk.py -i ../../../dados/Twitter/Aritter/raw/arriter_tweet_chunk_corpora.txt
# 
#produce twitter chunking results 
echo 'producing twitter ner results'
./spacy_ner.py -i ../../../dados/Twitter/Aritter/raw/arriter_tweet_ner_corpora.txt
# 
echo 'producing msm2013 twitter ner results'
./spacy_ner.py -i ../../../dados/MSM2013/tweets.txt



##########################
#SPACY CONLL
##########################
#
#produce conll pos results 
echo 'producing conll pos results'
./spacy_pos.py -i ../../../dados/Conll/raw/reuters.raw

#produce conll chunking results 
echo 'producing conll chunking results'
./spacy_chunk.py -i ../../../dados/Conll/raw/reuters.raw

# produce conll chunking results 
echo 'producing conll2000 chunking results'
./spacy_chunk.py -i /home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/dados/CoNLL-2000/raw/wsj2000.raw

echo 'producing conll ner results'
./spacy_ner.py -i ../../../dados/Conll/raw/reuters.raw