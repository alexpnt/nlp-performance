#!/usr/bin/env python2
# -*- coding: utf-8 -*-

def read_file_to_list(filename):

	with open(filename) as f:
		lines = f.readlines()

	tagged_sentences=[]
	sentence=[]
	for line in lines:
		# if line!='\n' and line!=' \n':
		if line!='\n':
			sentence+=[(line.split(" ")[0],line.split(" ")[1].rstrip("\n"))]
		else:
			tagged_sentences+=[sentence]
			sentence=[]

	return tagged_sentences

def correct_b_tags(annotated_file):

	chunk_filename="reuters.chunk.corrected"

	#read chunked sentences
	chunked_sentences=read_file_to_list(annotated_file)



	#correct it
	for i in xrange(len(chunked_sentences)):
		current_iob=chunked_sentences[i][0][1].split("-")[0]
		if current_iob is not 'O':														#Rule 0: Each document starts with the B- chunk	
			current_type=chunked_sentences[i][0][1].split("-")[1]						#first TYPE
			chunked_sentences[i][0]=(chunked_sentences[i][0][0],'B-'+current_type)


		for j in xrange(len(chunked_sentences[i])-1):
			try:
				current_iob=chunked_sentences[i][j][1].split("-")[0]			#current B/I/O
				current_type=chunked_sentences[i][j][1].split("-")[1]			#current TYPE
			except Exception, e:
				pass

			try:
				next_iob=chunked_sentences[i][j+1][1].split("-")[0]				#next B/I/O
				next_type=chunked_sentences[i][j+1][1].split("-")[1]			#next TYPE
			except Exception, e:
				pass

			if current_iob=='O':												#Rule 1: After a 'O' chunk, always appear a new B- chunk
				chunked_sentences[i][j+1]=(chunked_sentences[i][j+1][0],'B-'+next_type)

			if current_iob==next_iob=="I" and current_type!=next_type:			#Rule 2 : If the current and next token both start with 'I' and have different TYPEs, reassigns the next token to the 'B-' encoding		
				chunked_sentences[i][j+1]=(chunked_sentences[i][j+1][0],'B-'+next_type)


			if current_iob=='B' and next_iob=='I' and current_type!=next_type:			#Rule 3 : If the current token starts with tag 'B' and next token starts with 'I' and have the different TYPEs, reassigns the next token to the 'B-' encoding		
				chunked_sentences[i][j+1]=(chunked_sentences[i][j+1][0],'B-'+next_type)





	#write back corrected chunked sentence
	chunk_corrected_results=open(chunk_filename,"w")
	for sentence in chunked_sentences:
		for token_chunk in sentence:
			chunk_corrected_results.write(token_chunk[0]+" "+token_chunk[1]+"\n")
		chunk_corrected_results.write("\n")
	chunk_corrected_results.close()




if __name__ == '__main__':
	annotated_file="reuters.chunk"
	correct_b_tags(annotated_file)