##########################
#OPENLP TWITTER
##########################

#produce twitter pos results 
echo 'producing twitter pos results'
./opennlp_pos.py -i ../../../dados/Twitter/Aritter/raw/arriter_tweet_pos_corpora.txt


##########################
#OPENLP CONLL
##########################

#produce conll pos results 
echo 'producing conll pos results'
./opennlp_pos.py -i ../../../dados/Conll/raw/reuters.raw

