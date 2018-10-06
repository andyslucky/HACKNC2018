import nltk
from nltk.tokenize import sent_tokenize, word_tokenize


def process_sentence(sentence):
    try:
        print(word_tokenize(sentence))
    except Exception as e:
        print(str(e))

