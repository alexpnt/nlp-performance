##########################
#PATTERN TWITTER
##########################
#

#produce twitter pos results 
echo 'producing twitter pos results'
./pattern_pos.py -i ../../../dados/Twitter/Aritter/raw/arriter_tweet_pos_corpora.txt

#produce twitter chunking results 
echo 'producing twitter chunking results'
./pattern_chunk.py -i ../../../dados/Twitter/Aritter/raw/arriter_tweet_chunk_corpora.txt

##########################
#PATTERN CONLL
##########################
#
#produce conll pos results 
echo 'producing conll pos results'
./pattern_pos.py -i ../../../dados/Conll/raw/reuters.raw

#produce conll chunking results 
echo 'producing conll chunking results'
./pattern_chunk.py -i ../../../dados/Conll/raw/reuters.raw

#produce twitter chunking results 
echo 'producing conll2000 chunking results'
./pattern_chunk.py -i ../../../dados/CoNLL-2000/raw/wsj2000.raw