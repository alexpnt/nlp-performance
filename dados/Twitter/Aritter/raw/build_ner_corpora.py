filename="ner.txt"
corpora_name="arriter_tweet_ner_corpora.txt"

with open(filename) as f:
    lines = f.readlines()

corpora=[]
tweet=""
for word in lines:
	if word!='\t\n':
		tweet+=word.split('\t')[0]
		tweet+=" "
	else:
		corpora+=[tweet]
		tweet=""

#debug
# for tweet in corpora:
# 	print tweet

print corpora
fcorpora=open(corpora_name,"w")
for tweet in corpora:
  fcorpora.write("%s\n" % tweet)
fcorpora.close()