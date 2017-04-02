import sys

filename="eng.train.annotated"
reuters_annotated_name="reuters.annotated"

with open(filename) as f:
    reuters_with_headers = f.readlines()

reuters_annotated=open(reuters_annotated_name,"w")
for line in reuters_with_headers:
	if line!="-DOCSTART- -X- O O\n" and line!="\n":
		reuters_annotated.write("%s" % line)
reuters_annotated.close()