import sys

def write_annotated_files(annotated_file):

	pos_filename="wsj2000.pos"
	chunk_filename="wsj2000.chunk"

	#read
	with open(annotated_file) as f:
		lines = f.read().splitlines()

	fpos=open(pos_filename,"w")
	fchunk=open(chunk_filename,"w")
	for i in xrange(0,len(lines)):
		if lines[i]!='':
			conll_tokens=lines[i].split(" ")
			word=conll_tokens[0]
			pos=conll_tokens[1]
			chunk=conll_tokens[2]
			fpos.write("%s %s\n" % (word,pos))
			fchunk.write("%s %s\n" % (word,chunk))
		else:
			fpos.write("\n")
			fchunk.write("\n")
	fpos.close()
	fchunk.close()

if __name__ == '__main__':
	annotated_file="train.txt"
	write_annotated_files(annotated_file)




	