filename="chunk.txt"
corpora_name="arriter_tweet_chunk_corpora.txt"

with open(filename) as f:
    lines = f.readlines()

corpora=[]
tweet=""
for word in lines:
	if word!='\n':
		tweet+=word.split(' ')[0]
		tweet+=" "
	else:
		corpora+=[tweet]
		tweet=""

fcorpora=open(corpora_name,"w")
for tweet in corpora:
  fcorpora.write("%s\n" % tweet)
fcorpora.close()