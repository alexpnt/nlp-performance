import nltk
from nltk.corpus import conll2000
import pprint

class UnigramChunker(nltk.ChunkParserI):
    def __init__(self, train_sents): # [_code-unigram-chunker-constructor]
        train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)]      # word,tag,chunk
                      for sent in train_sents]
        self.tagger = nltk.UnigramTagger(train_data) # [_code-unigram-chunker-buildit]

    def parse(self, sentence): # [_code-unigram-chunker-parse]
        pos_tags = [pos for (word,pos) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        conlltags = [(word, pos, chunktag) for ((word,pos),chunktag)
                     in zip(sentence, chunktags)]
        return nltk.chunk.conlltags2tree(conlltags)



if __name__ == '__main__':
    # test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
    # train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])
    # unigram_chunker = UnigramChunker(train_sents)
    # print(unigram_chunker.evaluate(test_sents))

    # postags = sorted(set(pos for sent in train_sents for (word,pos) in sent.leaves()))
    # print(unigram_chunker.tagger.tag(postags))

    sent = nltk.corpus.treebank.tagged_sents()[22]
    print sent
    # print nltk.ne_chunk(sent,binary=False)

    print pprint.pformat(nltk.chunk.tree2conlltags(nltk.ne_chunk(sent,binary=False)))