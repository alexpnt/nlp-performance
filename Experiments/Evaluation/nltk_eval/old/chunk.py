import nltk.chunk
from nltk.corpus import conll2000
import itertools
 
def conll_tag_chunks(chunk_sents):
    tag_sents = [nltk.chunk.tree2conlltags(tree) for tree in chunk_sents]
    return [[(t, c) for (w, t, c) in chunk_tags] for chunk_tags in tag_sents]

class TagChunker(nltk.chunk.ChunkParserI):
    def __init__(self, train_sents): # [_code-unigram-chunker-constructor]
        train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)]      # word,tag,chunk
                      for sent in train_sents]
        self.tagger = nltk.UnigramTagger(train_data) # [_code-unigram-chunker-buildit]
 
    def parse(self, tokens):
		# split words and part of speech tags
		(words, tags) = zip(*tokens)
		# get IOB chunk tags
		chunks = self.tagger.tag(tags)
		print chunks
		# join words with chunk tags
		wtc = itertools.izip(words, chunks)
		# w = word, t = part-of-speech tag, c = chunk tag
		lines = [' '.join([w, t, c]) for (w, (t, c)) in wtc if c]
		# create tree from conll formatted chunk lines
		return nltk.chunk.conllstr2tree('\n'.join(lines))

if __name__ == '__main__':
	test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP','VP','PP'])
	train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP','VP','PP'])
	tagger=TagChunker(train_sents)

	# sentence should be a list of words
	sentence=["Hello","my","name","is","Alexandre"]
	tagged = tagger.parse(sentence)
