import sys

filename="eng.train.annotated"
reuters_annotated_name="reuters.pos.chunk.annotated"

with open(filename) as f:
    reuters_with_headers = f.readlines()

to_remove=[]
for i in xrange(len(reuters_with_headers)):
	if reuters_with_headers[i]=="-DOCSTART- -X- O O\n":
		to_remove+=[i]
		to_remove+=[i+1]

to_remove.reverse()
for index in to_remove:
	del reuters_with_headers[index]

reuters_annotated=open(reuters_annotated_name,"w")
for line in reuters_with_headers:
	if line !='\n':
		line_without_ner="".join(line.split(" ")[0]+" "+line.split(" ")[1]+" "+line.split(" ")[2]+"\n")
		reuters_annotated.write("%s" % line_without_ner)
	else:
		reuters_annotated.write("%s" % line)
reuters_annotated.close()

# 	if line!="-DOCSTART- -X- O O\n" and line!="\n":