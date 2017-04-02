filename="pos.txt"
corpora_name="arriter_tweet_pos_corpora.txt"

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

#debug
# for tweet in corpora:
# 	print tweet

fcorpora=open(corpora_name,"w")
for tweet in corpora:
  fcorpora.write("%s\n" % tweet)
fcorpora.close()