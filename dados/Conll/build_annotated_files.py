import sys

def write_annotated_files(annotated_file):

	pos_filename="reuters.pos"
	chunk_filename="reuters.chunk"
	ner_filename="reuters.ner"

	#read
	with open(annotated_file) as f:
		lines = f.read().splitlines()

	#remove empty strings
	lines=[line for line in lines if line]

	fpos=open(pos_filename,"w")
	fner=open(ner_filename,"w")
	fchunk=open(chunk_filename,"w")
	for i in xrange(1,len(lines)):
		if lines[i]!='-DOCSTART- -X- O O':
			conll_tokens=lines[i].split(" ")
			word=conll_tokens[0]
			pos=conll_tokens[1]
			chunk=conll_tokens[2]
			ner=conll_tokens[3]
			fpos.write("%s %s\n" % (word,pos))
			fchunk.write("%s %s\n" % (word,chunk))
			fner.write("%s %s\n" % (word,ner))
		else:
			fpos.write("\n")
			fchunk.write("\n")
			fner.write("\n")
	fpos.close()
	fner.close()
	fchunk.close()

if __name__ == '__main__':
	annotated_file="eng.train.annotated"
	write_annotated_files(annotated_file)




	