# ./aritter_pos.py -i /home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/dados/Twitter/Aritter/raw/arriter_tweet_pos_corpora.txt
# ./aritter_pos.py  -i /home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/dados/Conll/raw/reuters.raw

export TWITTER_NLP=../../../Experiments/Tools/twitter_nlp/
python2 ../../../Experiments/Tools/twitter_nlp/python/ner/extractEntities.py ../../../dados/CoNLL-2000/raw/wsj2000.raw -o ../../../Experiments/Evaluation/aritter/conll2000/compare/aritter_conll2000.chunk --classify --pos --chunk 