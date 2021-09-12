import urllib.request
from pathlib import Path

def download_file(url, output_file):
  Path(output_file).parent.mkdir(parents=True, exist_ok=True)
  urllib.request.urlretrieve (url, output_file)

download_file('https://raw.githubusercontent.com/ZihanWangKi/CrossWeigh/master/data/conllpp_train.txt', '/content/data/conllpp_train.txt')
download_file('https://raw.githubusercontent.com/ZihanWangKi/CrossWeigh/master/data/conllpp_dev.txt', '/content/data/conllpp_dev.txt')
download_file('https://raw.githubusercontent.com/ZihanWangKi/CrossWeigh/master/data/conllpp_test.txt', '/content/data/conllpp_test.txt')


from flair.data import Corpus
from flair.datasets import ColumnCorpus
columns = {0: 'text', 3: 'ner'}
corpus: Corpus = ColumnCorpus('/content/data/', columns,
                              train_file='conllpp_train.txt',
                              test_file='conllpp_test.txt',
                              dev_file='conllpp_dev.txt')




import pandas as pd
data = [[len(corpus.train), len(corpus.test), len(corpus.dev)]]
# Prints out the dataset sizes of train test and development in a table.
pd.DataFrame(data, columns=["Train", "Test", "Development"])




import flair
from typing import List
from flair.trainers import ModelTrainer
from flair.models import SequenceTagger
from flair.embeddings import TokenEmbeddings, WordEmbeddings, StackedEmbeddings, FlairEmbeddings

tag_type = 'ner'
tag_dictionary = corpus.make_tag_dictionary(tag_type=tag_type)

# For faster training and smaller models, we can comment out the flair embeddings.
# This will significantly affect the performance though.
embedding_types: List[TokenEmbeddings] = [
    WordEmbeddings('glove'),
    FlairEmbeddings('news-forward'),
    FlairEmbeddings('news-backward'),
]

embeddings: StackedEmbeddings = StackedEmbeddings(embeddings=embedding_types)

tagger: SequenceTagger = SequenceTagger(hidden_size=256,
                                        embeddings=embeddings,
                                        tag_dictionary=tag_dictionary,
                                        tag_type=tag_type,
                                        use_crf=True)

trainer: ModelTrainer = ModelTrainer(tagger, corpus)

trainer.train('/content/model/conllpp',
              learning_rate=0.1,
              mini_batch_size=32,
              max_epochs=50,
              embeddings_storage_mode='gpu')


from flair.data import Sentence
from flair.models import SequenceTagger

input_sentence = 'My name is Eugene, I currently live in Singapore, I work for DSO.'
tagger: SequenceTagger = SequenceTagger.load("/content/model/conllpp/final-model.pt")
sentence: Sentence = Sentence(input_sentence)
tagger.predict(sentence)
print(sentence.to_tagged_string())