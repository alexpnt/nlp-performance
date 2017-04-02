import sys

filename="train.txt"
corpora_name="wsj2000.raw"

#read
with open(filename) as f:
    lines = f.read().splitlines()

corpora=[]
article=""
for line in lines:
	if line!='':
		article+=line.split(' ')[0]
		article+=" "
	else:
		corpora+=[article]
		article=""

corpora+=[article]
article=""


#debug
# for article in corpora:
# 	print article
fcorpora=open(corpora_name,"w")
for article in corpora:
	fcorpora.write("%s\n" % article)
fcorpora.close()