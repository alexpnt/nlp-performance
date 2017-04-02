echo "Gathering statistics on the twitter dataset"
./stats.py -r /home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/dados/Twitter/Aritter/annotated/pos.txt > twitter_pos.txt
./stats.py -r /home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/dados/Twitter/Aritter/annotated/chunk.txt > twitter_chunk.txt
./stats.py -r /home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/dados/Twitter/Aritter/annotated/ner.txt > twitter_ner.txt
./stats.py -r /home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/dados/Twitter/Aritter/annotated/joint_ner.txt > twitter_joint_ner.txt
./stats.py -r /home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/dados/Twitter/Aritter/annotated/joint_ent_ner.txt > twitter_joint_ent_ner.txt

echo "Gathering statistics on the conll dataset"
./stats.py -r /home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/dados/Conll/annotated/reuters.pos > conll_pos.txt
./stats.py -r /home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/dados/Conll/annotated/reuters.chunk > conll_chunk.txt
./stats.py -r /home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/dados/Conll/annotated/reuters.ner > conll_ner.txt
./stats.py -r /home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/dados/Conll/annotated/reuters.joint.ner > conll_joint_ner.txt
./stats.py -r /home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/dados/Conll/annotated/reuters.joint.ent.ner > conll_joint_ent_ner.txt


echo "Gathering statistics on the #msm2013 dataset"
./stats.py -r /home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/dados/MSM2013/annotated/msm2013.ner > msm2013_ner.txt
./stats.py -r /home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/dados/MSM2013/annotated/msm2013.ent.ner > msm2013_ent_ner.txt
