import sys

filename="eng.train.annotated"
corpora_name="reuters.raw"

#read
with open(filename) as f:
    lines = f.read().splitlines()

#remove empty strings
lines=[line for line in lines if line]

corpora=[]
article=""
for line in lines:
	if line!='-DOCSTART- -X- O O':
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

corpora.pop(0)
fcorpora=open(corpora_name,"w")
for article in corpora:
	fcorpora.write("%s\n" % article)
fcorpora.close()