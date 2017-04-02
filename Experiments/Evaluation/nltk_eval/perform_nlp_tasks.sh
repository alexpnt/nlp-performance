##########################
#NLTK TWITTER
##########################
#
# produce twitter ner results 
echo 'producing twitter ner results'
./nltk_ner.py -i ../../../dados/Twitter/Aritter/raw/arriter_tweet_ner_corpora.txt

echo 'producing msm2013 ner results'
./nltk_ner.py -i ../../../dados/MSM2013/tweets.txt

echo 'producing twitter ner results'
./nltk_ner.py -i ../../../dados/Twitter/Aritter/raw/arriter_tweet_ner_corpora.txt

# #produce twitter pos results 
echo 'producing twitter pos results'
./nltk_pos.py -i ../../../dados/Twitter/Aritter/raw/arriter_tweet_pos_corpora.txt

# #produce twitter chunking results 
echo 'producing twitter chunking results'
./nltk_chunk.py -i ../../../dados/Twitter/Aritter/raw/arriter_tweet_chunk_corpora.txt

# ##########################
# #NLTK CONLL
# ##########################
# #
# #produce conll ner results 
echo 'producing conll ner results'
./nltk_ner.py -i ../../../dados/Conll/raw/reuters.raw

# #produce conll pos results 
echo 'producing conll pos results'
./nltk_pos.py -i ../../../dados/Conll/raw/reuters.raw

# #produce conll chunking results 
echo 'producing conll chunking results'
./nltk_chunk.py -i ../../../dados/Conll/raw/reuters.raw

# #produce conll 2000 chunking results 
echo 'producing conll 2000 chunking results'
./nltk_chunk.py -i ../../../dados/CoNLL-2000/raw/wsj2000.raw