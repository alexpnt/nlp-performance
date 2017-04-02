#########################
# NLTK TWITTER
#########################

# averaged_evaluation NLTK POS tagging
echo "Evaluating NLTK POS tagging on the twitter dataset"
./averaged_evaluation.py -r ../../dados/Twitter/Aritter/annotated/pos.txt -p ../../Experiments/Evaluation/nltk_eval/twitter/compare/nltk_pos_output.txt > ../../Experiments/Evaluation/nltk_eval/twitter/results/pos_performance.txt

# #averaged_evaluation NLTK NER tagging
echo "Evaluating NLTK NER tagging on the twitter dataset"
./averaged_evaluation.py -r ../../dados/Twitter/Aritter/annotated/joint_ner.txt -p ../../Experiments/Evaluation/nltk_eval/twitter/compare/nltk_joint_ner_output.txt > ../../Experiments/Evaluation/nltk_eval/twitter/results/joint_ner_performance.txt

# averaged_evaluation NLTK NEC tagging
echo "Evaluating NLTK NEC tagging on the twitter dataset"
./averaged_evaluation.py -r ../../dados/Twitter/Aritter/annotated/joint_ent_ner.txt -p ../../Experiments/Evaluation/nltk_eval/twitter/compare/nltk_joint_ent_ner_output.txt > ../../Experiments/Evaluation/nltk_eval/twitter/results/joint_ent_ner_performance.txt


echo "Evaluating NLTK NER tagging on the msm2013 dataset"
./averaged_evaluation.py -r ../../dados/MSM2013/annotated/msm2013.ner -p ../../Experiments/Evaluation/nltk_eval/msm2013/compare/nltk_joint_ner_output.txt > ../../Experiments/Evaluation/nltk_eval/msm2013/results/joint_ner_performance.txt

echo "Evaluating NLTK NEC tagging on the msm2013 dataset"
./averaged_evaluation.py -r ../../dados/MSM2013/annotated/msm2013.ent.ner -p ../../Experiments/Evaluation/nltk_eval/msm2013/compare/nltk_joint_ent_ner_output.txt > ../../Experiments/Evaluation/nltk_eval/msm2013/results/joint_ent_ner_performance.txt

# #averaged_evaluation NLTK Chunk tagging
echo "Evaluating NLTK Chunk tagging on the twitter dataset"
./averaged_evaluation.py -r ../../dados/Twitter/Aritter/annotated/chunk.txt -p ../../Experiments/Evaluation/nltk_eval/twitter/compare/nltk_chunk_output_ready.txt > ../../Experiments/Evaluation/nltk_eval/twitter/results/chunk_performance.txt

#########################
# NLTK CONLL
#########################

# averaged_evaluation NLTK POS tagging
echo "Evaluating NLTK POS tagging on the conll dataset"
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.pos -p ../../Experiments/Evaluation/nltk_eval/conll/compare/nltk_pos_output.txt > ../../Experiments/Evaluation/nltk_eval/conll/results/pos_performance.txt

#averaged_evaluation NLTK NER tagging
echo "Evaluating NLTK NER tagging on the conll dataset"
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.joint.ner -p  ../../Experiments/Evaluation/nltk_eval/conll/compare/nltk_joint_ner_output.txt > ../../Experiments/Evaluation/nltk_eval/conll/results/joint_ner_performance.txt

#averaged_evaluation NLTK Chunk tagging
echo "Evaluating NLTK Chunk tagging on the conll dataset"
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.chunk -p ../../Experiments/Evaluation/nltk_eval/conll/compare/nltk_chunk_output.txt > ../../Experiments/Evaluation/nltk_eval/conll/results/chunk_performance.txt

# averaged_evaluation NLTK Chunk tagging
echo "Evaluating NLTK Chunk tagging on the conll2000 dataset"
./averaged_evaluation.py -r ../../dados/CoNLL-2000/annotated/wsj2000.chunk  -p ../../Experiments/Evaluation/nltk_eval/conll2000/compare/nltk_chunk_output.txt > ../../Experiments/Evaluation/nltk_eval/conll2000/results/nltk_chunk_performance.txt

# averaged_evaluation NLTK Chunk tagging
echo "Evaluating NLTK Chunk tagging on the conll2003 dataset"
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.chunk.corrected -p ../../Experiments/Evaluation/nltk_eval/conll/compare/nltk_chunk_output.txt > ../../Experiments/Evaluation/nltk_eval/conll/results/chunk_corrected_performance.txt


# averaged_evaluation NLTK NER tagging
echo "Evaluating NLTK NEC tagging on the conll dataset"
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.joint.ent.ner -p  ../../Experiments/Evaluation/nltk_eval/conll/compare/nltk_joint_ent_ner_output.txt > ../../Experiments/Evaluation/nltk_eval/conll/results/joint_ent_ner_performance.txt




#########################
# OPENNLP TWITTER
#########################

# averaged_evaluation OPENNLP POS tagging
echo "Evaluating OPENNLP POS tagging on the twitter dataset"
./averaged_evaluation.py -r ../../dados/Twitter/Aritter/annotated/pos.txt -p ../../Experiments/Evaluation/apache_opennlp/twitter/compare/opennlp_pos_output.txt > ../../Experiments/Evaluation/apache_opennlp/twitter/results/pos_performance.txt

# averaged_evaluation OPENNLP CHUNK tagging
echo "Evaluating OPENNLP Chunk tagging on the twitter dataset"
./averaged_evaluation.py -r ../../dados/Twitter/Aritter/annotated/chunk.upper.txt -p ../../Experiments/Evaluation/apache_opennlp/twitter/compare/opennlp_aritter.chunk > ../../Experiments/Evaluation/apache_opennlp/twitter/results/chunk_performance.txt

echo "Evaluating OPENNLP NER tagging on the twitter dataset"
./averaged_evaluation.py -r ../../dados/Twitter/Aritter/annotated/joint_ner.txt -p ../../Experiments/Evaluation/apache_opennlp/twitter/compare/opennlp_aritter.ner > ../../Experiments/Evaluation/apache_opennlp/twitter/results/ner_performance.txt

echo "Evaluating OPENNLP NEC tagging on the twitter dataset"
./averaged_evaluation.py -r ../../dados/Twitter/Aritter/annotated/joint_ent_ner.txt -p ../../Experiments/Evaluation/apache_opennlp/twitter/compare/opennlp_aritter.ent.ner > ../../Experiments/Evaluation/apache_opennlp/twitter/results/ent_ner_performance.txt



echo "Evaluating OPENNLP NER tagging on the msm2013 dataset"
./averaged_evaluation.py -r ../../dados/MSM2013/annotated/msm2013.ner -p ../../Experiments/Evaluation/apache_opennlp/msm2013/compare/opennlp_msm2013.ner > ../../Experiments/Evaluation/apache_opennlp/msm2013/results/ner_performance.txt

echo "Evaluating OPENNLP NEC tagging on the msm2013 dataset"
./averaged_evaluation.py -r ../../dados/MSM2013/annotated/msm2013.ent.ner -p ../../Experiments/Evaluation/apache_opennlp/msm2013/compare/opennlp_msm2013.ent.ner > ../../Experiments/Evaluation/apache_opennlp/msm2013/results/ent_ner_performance.txt

# PERCEPTRON

# averaged_evaluation OPENNLP POS tagging
echo "Evaluating OPENNLP POS tagging on the twitter dataset"
./averaged_evaluation.py -r ../../dados/Twitter/Aritter/annotated/pos.txt -p ../../Experiments/Evaluation/apache_opennlp/twitter/compare/perceptron/opennlp_pos_output.txt > ../../Experiments/Evaluation/apache_opennlp/twitter/results/perceptron/pos_performance.txt

# averaged_evaluation OPENNLP CHUNK tagging
echo "Evaluating OPENNLP Chunk tagging on the twitter dataset"
./averaged_evaluation.py -r ../../dados/Twitter/Aritter/annotated/chunk.upper.txt -p ../../Experiments/Evaluation/apache_opennlp/twitter/compare/perceptron/opennlp_aritter.chunk > ../../Experiments/Evaluation/apache_opennlp/twitter/results/perceptron/chunk_performance.txt

echo "Evaluating OPENNLP NER tagging on the twitter dataset"
./averaged_evaluation.py -r ../../dados/Twitter/Aritter/annotated/joint_ner.txt -p ../../Experiments/Evaluation/apache_opennlp/twitter/compare/perceptron/opennlp_aritter.ner > ../../Experiments/Evaluation/apache_opennlp/twitter/results/perceptron/ner_performance.txt

echo "Evaluating OPENNLP NEC tagging on the twitter dataset"
./averaged_evaluation.py -r ../../dados/Twitter/Aritter/annotated/joint_ent_ner.txt -p ../../Experiments/Evaluation/apache_opennlp/twitter/compare/perceptron/opennlp_aritter.ent.ner > ../../Experiments/Evaluation/apache_opennlp/twitter/results/perceptron/ent_ner_performance.txt

echo "Evaluating OPENNLP NER tagging on the msm2013 dataset"
./averaged_evaluation.py -r ../../dados/MSM2013/annotated/msm2013.ner -p ../../Experiments/Evaluation/apache_opennlp/msm2013/compare/perceptron/opennlp_msm2013.ner > ../../Experiments/Evaluation/apache_opennlp/msm2013/results/perceptron/ner_performance.txt

echo "Evaluating OPENNLP NEC tagging on the msm2013 dataset"
./averaged_evaluation.py -r ../../dados/MSM2013/annotated/msm2013.ent.ner -p ../../Experiments/Evaluation/apache_opennlp/msm2013/compare/perceptron/opennlp_msm2013.ent.ner > ../../Experiments/Evaluation/apache_opennlp/msm2013/results/perceptron/ent_ner_performance.txt



#########################
# OPENNLP CONLL
#########################

# averaged_evaluation OPENNLP POS tagging
echo "Evaluating OPENNLP POS tagging on the conll dataset"
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.pos -p ../../Experiments/Evaluation/apache_opennlp/conll/compare/opennlp_pos_output.txt > ../../Experiments/Evaluation/apache_opennlp/conll/results/pos_performance.txt

echo "Evaluating OPENNLP Chunk tagging on the conll dataset"
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.chunk -p ../../Experiments/Evaluation/apache_opennlp/conll/compare/opennlp_reuters.chunk > ../../Experiments/Evaluation/apache_opennlp/conll/results/chunk_performance.txt

echo "Evaluating OPENNLP NER tagging on the conll dataset"
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.joint.ner -p ../../Experiments/Evaluation/apache_opennlp/conll/compare/opennlp_reuters.ner > ../../Experiments/Evaluation/apache_opennlp/conll/results/ner_performance.txt

echo "Evaluating OPENNLP NEC tagging on the conll dataset"
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.joint.ent.ner -p ../../Experiments/Evaluation/apache_opennlp/conll/compare/opennlp_reuters.ent.ner > ../../Experiments/Evaluation/apache_opennlp/conll/results/ent_ner_performance.txt

echo "Evaluating OPENNLP Chunk tagging on the conll2003 dataset"
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.chunk.corrected -p ../../Experiments/Evaluation/apache_opennlp/conll/compare/opennlp_reuters.chunk > ../../Experiments/Evaluation/apache_opennlp/conll/results/chunk_performance_corrected.txt

# PERCEPTRON


# averaged_evaluation OPENNLP POS tagging
echo "Evaluating OPENNLP POS tagging on the conll dataset"
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.pos -p ../../Experiments/Evaluation/apache_opennlp/conll/compare/perceptron/opennlp_pos_output.txt > ../../Experiments/Evaluation/apache_opennlp/conll/results/perceptron/pos_performance.txt

echo "Evaluating OPENNLP Chunk tagging on the conll dataset"
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.chunk -p ../../Experiments/Evaluation/apache_opennlp/conll/compare/perceptron/opennlp_reuters.chunk > ../../Experiments/Evaluation/apache_opennlp/conll/results/perceptron/chunk_performance.txt

echo "Evaluating OPENNLP NER tagging on the conll dataset"
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.joint.ner -p ../../Experiments/Evaluation/apache_opennlp/conll/compare/perceptron/opennlp_reuters.ner > ../../Experiments/Evaluation/apache_opennlp/conll/results/perceptron/ner_performance.txt

echo "Evaluating OPENNLP NEC tagging on the conll dataset"
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.joint.ent.ner -p ../../Experiments/Evaluation/apache_opennlp/conll/compare/perceptron/opennlp_reuters.ent.ner > ../../Experiments/Evaluation/apache_opennlp/conll/results/perceptron/ent_ner_performance.txt

echo "Evaluating OPENNLP Chunk tagging on the conll2013 dataset"
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.chunk.corrected -p ../../Experiments/Evaluation/apache_opennlp/conll/compare/perceptron/opennlp_reuters.chunk > ../../Experiments/Evaluation/apache_opennlp/conll/results/perceptron/chunk_performance_corrected.txt


#########################
# OPENNLP TWITTER
#########################

# averaged_evaluation OPENNLP POS tagging
echo "Evaluating OPENNLP POS tagging on the twitter dataset"
./averaged_evaluation.py -r ../../dados/Twitter/Aritter/annotated/pos.txt -p ../../Experiments/Evaluation/apache_opennlp/twitter/compare/opennlp_pos_output.txt > ../../Experiments/Evaluation/apache_opennlp/twitter/results/pos_performance.txt


#########################
# OPENNLP CONLL
#########################

# averaged_evaluation OPENNLP POS tagging
echo "Evaluating OPENNLP POS tagging on the conll dataset"
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.pos -p ../../Experiments/Evaluation/apache_opennlp/conll/compare/opennlp_pos_output.txt > ../../Experiments/Evaluation/apache_opennlp/conll/results/pos_performance.txt

echo "Evaluating OPENNLP Chunk tagging on the conll 2000 dataset"
./averaged_evaluation.py -r ../../dados/CoNLL-2000/annotated/wsj2000.chunk -p ../../Experiments/Evaluation/apache_opennlp/conll2000/compare/opennlp_wsj2000.chunk > ../../Experiments/Evaluation/apache_opennlp/conll2000/results/opennlp_wsj2000.performance



#########################
# CMU TWITTER
#########################

# averaged_evaluation OPENNLP POS tagging
echo "Evaluating CMU POS tagging on the twitter dataset"
./averaged_evaluation.py -r ../../dados/Twitter/Aritter/annotated/pos.txt -p ../../Experiments/Evaluation/cmu_tweet_nlp/twitter/compare/cmu_tweetnlp_pos_output.txt > ../../Experiments/Evaluation/cmu_tweet_nlp/twitter/results/pos_performance.txt


#########################
# CMU CONLL
#########################

# averaged_evaluation OPENNLP POS tagging
echo "Evaluating CMU POS tagging on the conll dataset"
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.pos -p ../../Experiments/Evaluation/cmu_tweet_nlp/conll/compare/cmu_tweetnlp_pos_output.txt > ../../Experiments/Evaluation/cmu_tweet_nlp/conll/results/pos_performance.txt




#########################
# STANFORD TWITTER
#########################

# averaged_evaluation OPENNLP POS tagging
echo "Evaluating STANFORD POS tagging on the twitter dataset"
./averaged_evaluation.py -r ../../dados/Twitter/Aritter/annotated/pos.txt -p ../../Experiments/Evaluation/stanford_nlp/twitter/compare/stanford_nlp_pos_output.txt > ../../Experiments/Evaluation/stanford_nlp/twitter/results/pos_performance.txt


echo "Evaluating STANFORD NER tagging on the twitter dataset"
./averaged_evaluation.py -r ../../dados/Twitter/Aritter/annotated/joint_ner.txt -p ../../Experiments/Evaluation/stanford_nlp/twitter/compare/stanford_nlp_joint_ner_output.txt > ../../Experiments/Evaluation/stanford_nlp/twitter/results/joint_ner_performance.txt

echo "Evaluating STANFORD NEC tagging on the twitter dataset"
./averaged_evaluation.py -r ../../dados/Twitter/Aritter/annotated/joint_ent_ner.txt -p ../../Experiments/Evaluation/stanford_nlp/twitter/compare/stanford_nlp_joint_ent_ner_output.txt > ../../Experiments/Evaluation/stanford_nlp/twitter/results/joint_ent_ner_performance.txt


echo "Evaluating STANFORD NER tagging on the msm2013 dataset"
./averaged_evaluation.py -r ../../dados/MSM2013/annotated/msm2013.ner -p ../../Experiments/Evaluation/stanford_nlp/msm2013/compare/stanford_nlp_joint_ner_output.txt > ../../Experiments/Evaluation/stanford_nlp/msm2013/results/joint_ner_performance.txt

echo "Evaluating STANFORD NEC tagging on the msm2013 dataset"
./averaged_evaluation.py -r ../../dados/MSM2013/annotated/msm2013.ent.ner -p ../../Experiments/Evaluation/stanford_nlp/msm2013/compare/stanford_nlp_joint_ent_ner_output.txt > ../../Experiments/Evaluation/stanford_nlp/msm2013/results/joint_ent_ner_performance.txt

#########################
# STANFORD CONLL
#########################

# averaged_evaluation OPENNLP POS tagging
echo "Evaluating STANFORD POS tagging on the conll dataset"
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.ner -p ../../Experiments/Evaluation/stanford_nlp/conll/compare/stanford_nlp_ner_output.txt > ../../Experiments/Evaluation/stanford_nlp/conll/results/ner_performance.txt

echo "Evaluating STANFORD NER tagging on the conll dataset"
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.joint.ner -p ../../Experiments/Evaluation/stanford_nlp/conll/compare/stanford_nlp_joint_ner_output.txt > ../../Experiments/Evaluation/stanford_nlp/conll/results/joint_ner_performance.txt

echo "Evaluating STANFORD NEC tagging on the conll dataset"
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.joint.ent.ner -p ../../Experiments/Evaluation/stanford_nlp/conll/compare/stanford_nlp_joint_ent_ner_output.txt > ../../Experiments/Evaluation/stanford_nlp/conll/results/joint_ent_ner_performance.txt


#########################
# ARITTER TWITTER
#########################
echo "Evaluating ARITTER POS tagging on the twitter dataset"
./averaged_evaluation.py -r ../../dados/Twitter/Aritter/annotated/pos.txt -p ../../Experiments/Evaluation/aritter/twitter/compare/aritter_pos_output.txt > ../../Experiments/Evaluation/aritter/twitter/results/pos_performance.txt

echo "Evaluating ARITTER CHUNKING tagging on the twitter dataset"
./averaged_evaluation.py -r ../../dados/Twitter/Aritter/annotated/chunk.txt -p ../../Experiments/Evaluation/aritter/twitter/compare/aritter_chunk_output.txt > ../../Experiments/Evaluation/aritter/twitter/results/chunk_performance.txt

echo "Evaluating ARITTER NER tagging on the twitter dataset"
./averaged_evaluation.py -r ../../dados/Twitter/Aritter/annotated/ner.txt -p ../../Experiments/Evaluation/aritter/twitter/compare/aritter_ner_output.txt > ../../Experiments/Evaluation/aritter/twitter/results/ner_performance.txt

echo "Evaluating ARITTER NER tagging on the twitter dataset"
./averaged_evaluation.py -r ../../dados/Twitter/Aritter/annotated/joint_ner.txt -p ../../Experiments/Evaluation/aritter/twitter/compare/aritter_joint_ner_output.txt > ../../Experiments/Evaluation/aritter/twitter/results/joint_ner_performance.txt

echo "Evaluating ARITTER NEC tagging on the twitter dataset"
./averaged_evaluation.py -r ../../dados/Twitter/Aritter/annotated/joint_ent_ner.txt -p ../../Experiments/Evaluation/aritter/twitter/compare/aritter_joint_ent_ner_output.txt > ../../Experiments/Evaluation/aritter/twitter/results/joint_ent_ner_performance.txt

echo "Evaluating ARITTTER NER tagging on the msm2013 dataset"
./averaged_evaluation.py -r ../../dados/MSM2013/annotated/msm2013.ner -p ../../Experiments/Evaluation/aritter/msm2013/compare/aritter_joint_ner_output.txt > ../../Experiments/Evaluation/aritter/msm2013/results/joint_ner_performance.txt

echo "Evaluating ARITTTER NEC tagging on the msm2013 dataset"
./averaged_evaluation.py -r ../../dados/MSM2013/annotated/msm2013.ent.ner -p ../../Experiments/Evaluation/aritter/msm2013/compare/aritter_joint_ent_ner_output.txt > ../../Experiments/Evaluation/aritter/msm2013/results/joint_ent_ner_performance.txt

#########################
# ARITTER CONLL
#########################

echo "Evaluating ARITTER POS tagging on the conll dataset"
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.pos -p ../../Experiments/Evaluation/aritter/conll/compare/aritter_pos_output.txt > ../../Experiments/Evaluation/aritter/conll/results/pos_performance.txt

echo "Evaluating ARITTER CHUNK tagging on the conll dataset"
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.chunk -p ../../Experiments/Evaluation/aritter/conll/compare/aritter_chunk_output_ready.txt > ../../Experiments/Evaluation/aritter/conll/results/chunk_performance.txt

echo "Evaluating ARITTER CHUNK tagging on the conll2000 dataset"
./averaged_evaluation.py -r ../../dados/CoNLL-2000/annotated/wsj2000.chunk -p ../../Experiments/Evaluation/aritter/conll2000/compare/aritter_conll2000.iob.chunk > ../../Experiments/Evaluation/aritter/conll2000/results/aritter_conll2000.chunk.performance

echo "Evaluating ARITTER NER tagging on the conll dataset"
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.joint.ner -p ../../Experiments/Evaluation/aritter/conll/compare/aritter_joint_ner_output.txt > ../../Experiments/Evaluation/aritter/conll/results/joint_ner_performance.txt

echo "Evaluating ARITTER NEC tagging on the conll dataset"
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.joint.ent.ner -p ../../Experiments/Evaluation/aritter/conll/compare/aritter_joint_ent_ner_output.txt > ../../Experiments/Evaluation/aritter/conll/results/joint_ent_ner_performance.txt

echo "Evaluating ARITTER CHUNK tagging on the conll2003 dataset"
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.chunk.corrected -p ../../Experiments/Evaluation/aritter/conll/compare/aritter_chunk_output_ready.txt > ../../Experiments/Evaluation/aritter/conll/results/chunk_performance_corrected.txt

#########################
# PATTERN TWITTER
#########################

# averaged_evaluation NLTK POS tagging
echo "Evaluating PATTERN POS tagging on the twitter dataset"
./averaged_evaluation.py -r ../../dados/Twitter/Aritter/annotated/pos.txt -p ../../Experiments/Evaluation/pattern/twitter/compare/pattern_pos_output.txt > ../../Experiments/Evaluation/pattern/twitter/results/pos_performance.txt

# #averaged_evaluation NLTK Chunk tagging
echo "Evaluating PATTERN Chunk tagging on the twitter dataset"
./averaged_evaluation.py -r ../../dados/Twitter/Aritter/annotated/chunk.txt -p ../../Experiments/Evaluation/pattern/twitter/compare/pattern_chunk_output.txt > ../../Experiments/Evaluation/pattern/twitter/results/chunk_performance.txt

#########################
# PATTERN CONLL
#########################

# averaged_evaluation Pattern POS tagging
echo "Evaluating PATTERN POS tagging on the conll dataset"The/O/DT/B-NP
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.pos -p ../../Experiments/Evaluation/pattern/conll/compare/pattern_pos_output.txt > ../../Experiments/Evaluation/pattern/conll/results/pos_performance.txt

# #averaged_evaluation Pattern Chunk tagging
echo "Evaluating PATTERN Chunk tagging on the conll dataset"
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.chunk -p ../../Experiments/Evaluation/pattern/conll/compare/pattern_chunk_output.txt > ../../Experiments/Evaluation/pattern/conll/results/chunk_performance.txt


# #averaged_evaluation Pattern Chunk tagging
echo "Evaluating PATTERN Chunk tagging on the conll2000 dataset"
./averaged_evaluation.py -r ../../dados/CoNLL-2000/annotated/wsj2000.chunk -p ../../Experiments/Evaluation/pattern/conll2000/compare/pattern_chunk_output.txt > ../../Experiments/Evaluation/pattern/conll2000/results/pattern_chunk_performance.txt

#averaged_evaluation Pattern Chunk tagging
echo "Evaluating PATTERN Chunk tagging on the conll2003 dataset"
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.chunk.corrected -p ../../Experiments/Evaluation/pattern/conll/compare/pattern_chunk_output.txt > ../../Experiments/Evaluation/pattern/conll/results/chunk_performance_corrected.txt


#########################
# TwitIE TWITTER
#########################

# averaged_evaluation TwitIE POS tagging
echo "Evaluating TwitIE POS tagging on the twitter dataset"
./averaged_evaluation.py -r ../../dados/Twitter/Aritter/annotated/pos.txt -p ../../Experiments/Evaluation/OntoText/twitter/compare/arriter_tweet_pos_corpora.txt_pos_annotated.txt > ../../Experiments/Evaluation/OntoText/twitter/results/aritter_pos_performance.txt

#averaged_evaluation TwitIE NEC tagging
echo "Evaluating TwitIE NEC tagging on the twitter dataset"
./averaged_evaluation.py -r ../../dados/Twitter/Aritter/annotated/joint_ner.txt -p ../../Experiments/Evaluation/OntoText/twitter/compare/arriter_tweet_ner_corpora.txt_ner_annotated.txt> ../../Experiments/Evaluation/OntoText/twitter/results/arriter_ner_performance.txt

echo "Evaluating TwitIE NER tagging on the twitter dataset"
./averaged_evaluation.py -r ../../dados/Twitter/Aritter/annotated/joint_ent_ner.txt -p ../../Experiments/Evaluation/OntoText/twitter/compare/arriter_tweet_ent_ner_corpora.txt_ner_annotated.txt > ../../Experiments/Evaluation/OntoText/twitter/results/arriter_ent_ner_performance.txt

echo "Evaluating TwitIE NEC tagging on the msm2013 dataset"
./averaged_evaluation.py -r ../../dados/MSM2013/annotated/msm2013.ner -p ../../Experiments/Evaluation/OntoText/twitter/compare/tweets.txt_ner_annotated.txt > ../../Experiments/Evaluation/OntoText/twitter/results/msm2013_ner_performance.txt


echo "Evaluating TwitIE NER tagging on the msm2013 dataset"
./averaged_evaluation.py -r ../../dados/MSM2013/annotated/msm2013.ent.ner -p ../../Experiments/Evaluation/OntoText/twitter/compare/tweets.txt_ent_ner_annotated.txt > ../../Experiments/Evaluation/OntoText/twitter/results/msm2013_ent_ner_performance.txt

#########################
# TwitIE CoNLL
#########################

# averaged_evaluation TwitIE POS tagging
echo "Evaluating TwitIE POS tagging on the conll dataset"
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.pos -p ../../Experiments/Evaluation/OntoText/conll/compare/reuters.raw_pos_annotated.txt > ../../Experiments/Evaluation/OntoText/conll/results/reuters.pos.performance.txt

# averaged_evaluation TwitIE NEC tagging
echo "Evaluating TwitIE NEC tagging on the conll dataset"
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.joint.ner -p  ../../Experiments/Evaluation/OntoText/conll/compare/reuters.raw_ner_annotated.txt > ../../Experiments/Evaluation/OntoText/conll/results/reuters.ner.performance.txt

# averaged_evaluation TwitIE NER tagging
echo "Evaluating TwitIE NER tagging on the conll dataset"
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.joint.ent.ner -p  ../../Experiments/Evaluation/OntoText/conll/compare/reuters.raw_ent_ner_annotated.txt > ../../Experiments/Evaluation/OntoText/conll/results/reuters.ent.ner.performance.txt


#########################
# SPACY TWITTER
#########################

# averaged_evaluation SPACY POS tagging
echo "Evaluating SPACY POS tagging on the twitter dataset"
./averaged_evaluation.py -r ../../dados/Twitter/Aritter/annotated/pos.txt -p ../../Experiments/Evaluation/spaCy/twitter/compare/spacy_pos_output.txt > ../../Experiments/Evaluation/spaCy/twitter/results/pos_performance.txt

#averaged_evaluation SPACY NER tagging
echo "Evaluating SPACY NER tagging on the twitter dataset"
./averaged_evaluation.py -r ../../dados/Twitter/Aritter/annotated/joint_ner.txt -p ../../Experiments/Evaluation/spaCy/twitter/compare/spacy_ner_output.txt > ../../Experiments/Evaluation/spaCy/twitter/results/joint_ner_performance.txt

# averaged_evaluation SPACY NEC tagging
echo "Evaluating SPACY NEC tagging on the twitter dataset"
./averaged_evaluation.py -r ../../dados/Twitter/Aritter/annotated/joint_ent_ner.txt -p ../../Experiments/Evaluation/spaCy/twitter/compare/spacy_joint_ent_ner_output.txt > ../../Experiments/Evaluation/spaCy/twitter/results/joint_ent_ner_performance.txt


echo "Evaluating SPACY NER tagging on the msm2013 dataset"
./averaged_evaluation.py -r ../../dados/MSM2013/annotated/msm2013.ner -p ../../Experiments/Evaluation/spaCy/msm2013/compare/spacy_ner_output.txt > ../../Experiments/Evaluation/spaCy/msm2013/results/joint_ner_performance.txt

echo "Evaluating SPACY NEC tagging on the msm2013 dataset"
./averaged_evaluation.py -r ../../dados/MSM2013/annotated/msm2013.ent.ner -p ../../Experiments/Evaluation/spaCy/msm2013/compare/spacy_joint_ent_ner_output.txt > ../../Experiments/Evaluation/spaCy/msm2013/results/joint_ent_ner_performance.txt

#averaged_evaluation SPACY Chunk tagging
echo "Evaluating SPACY Chunk tagging on the twitter dataset"
./averaged_evaluation.py -r ../../dados/Twitter/Aritter/annotated/chunk.txt -p ../../Experiments/Evaluation/spaCy/twitter/compare/spacy_chunk_output_ready.txt > ../../Experiments/Evaluation/spaCy/twitter/results/chunk_performance.txt


#########################
# SPACY CONLL
#########################

# averaged_evaluation SPACY POS tagging
echo "Evaluating SPACY POS tagging on the conll dataset"
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.pos -p ../../Experiments/Evaluation/spaCy/conll/compare/spacy_pos_output.txt > ../../Experiments/Evaluation/spaCy/conll/results/pos_performance.txt

#averaged_evaluation SPACY NER tagging
echo "Evaluating SPACY NER tagging on the conll dataset"
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.joint.ner -p  ../../Experiments/Evaluation/spaCy/conll/compare/spacy_ner_output.txt > ../../Experiments/Evaluation/spaCy/conll/results/joint_ner_performance.txt

#averaged_evaluation SPACY Chunk tagging
echo "Evaluating SPACY Chunk tagging on the conll dataset"
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.chunk -p ../../Experiments/Evaluation/spaCy/conll/compare/spacy_chunk_output.txt > ../../Experiments/Evaluation/spaCy/conll/results/chunk_performance.txt

# averaged_evaluation SPACY Chunk tagging
echo "Evaluating SPACY Chunk tagging on the conll2000 dataset"
./averaged_evaluation.py -r ../../dados/CoNLL-2000/annotated/wsj2000.chunk  -p ../../Experiments/Evaluation/spaCy/conll2000/compare/spacy_chunk_output.txt > ../../Experiments/Evaluation/spaCy/conll2000/results/spacy_chunk_performance.txt

# averaged_evaluation SPACY Chunk tagging
echo "Evaluating SPACY Chunk tagging on the conll2003 dataset"
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.chunk.corrected -p ../../Experiments/Evaluation/spaCy/conll/compare/spacy_chunk_output.txt > ../../Experiments/Evaluation/spaCy/conll/results/chunk_corrected_performance.txt


# averaged_evaluation SPACY NER tagging
echo "Evaluating SPACY NEC tagging on the conll dataset"
./averaged_evaluation.py -r ../../dados/Conll/annotated/reuters.joint.ent.ner -p  ../../Experiments/Evaluation/spaCy/conll/compare/spacy_ner_output.txt > ../../Experiments/Evaluation/spaCy/conll/results/joint_ent_ner_performance.txt
