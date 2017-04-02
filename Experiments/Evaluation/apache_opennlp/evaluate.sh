#!/bin/bash

#CONLL

#conll chunking
../../Tools/apache-opennlp-1.6.0/bin/opennlp ChunkerEvaluator -model "../../Tools/apache-opennlp-1.6.0/models/en-chunker.bin" -data "/home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/dados/Conll/annotated/reuters.pos.chunk.annotated" -detailedF true -misclassified false > conll/results/chunk_performance.txt

#conll tokenizer
../../Tools/apache-opennlp-1.6.0/bin/opennlp TokenizerMEEvaluator -model "../../Tools/apache-opennlp-1.6.0/models/en-token.bin" -data "/home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/dados/Conll/raw/reuters.raw" -misclassified false > conll/results/tokenizer_performance.txt

#conll pos


#TWITTER

#twitter chunking
../../Tools/apache-opennlp-1.6.0/bin/opennlp ChunkerEvaluator -model "../../Tools/apache-opennlp-1.6.0/models/en-chunker.bin" -data "/home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/dados/Twitter/Aritter/annotated/twitter.pos.chunk.annotated" -detailedF true -misclassified false > twitter/results/chunk_performance.txt

#twitter tokenizer
../../Tools/apache-opennlp-1.6.0/bin/opennlp TokenizerMEEvaluator -model "../../Tools/apache-opennlp-1.6.0/models/en-token.bin" -data "/home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/dados/Twitter/Aritter/raw/arriter_tweet_chunk_corpora.txt" -misclassified false > twitter/results/tokenizer_performance.txt

#twitter pos

exit 0