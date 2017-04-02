##########################
#TwitIE TWITTER
##########################
#

echo 'producing aritter twitter pos results'
./twitie.py -i ../../../dados/Twitter/Aritter/raw/arriter_tweet_pos_corpora.txt

echo 'producing aritter twitter ner results'
./twitie.py -i ../../../dados/Twitter/Aritter/raw/arriter_tweet_ner_corpora.txt

echo 'producing msm2013 ner results'
./twitie.py -i ../../../dados/MSM2013/tweets.txt


# ##########################
# #TwitIE CONLL
# ##########################

echo 'producing conll pos and ner results'
./twitie.py -i ../../../dados/Conll/raw/reuters.raw