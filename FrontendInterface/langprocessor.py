import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer

def stemWords(wordList):
    ps = PorterStemmer()
    stemmedWords = []
    for w in wordList:
        stemmedWords.append(ps.stem(w))

    return stemmedWords


def words_to_commands(sentence):
    print("test")

    return []


def process_sentence(sentence):
    try:
        sentenceWordsTokenized = word_tokenize(sentence)
        sentenceStemmed = stemWords(sentenceWordsTokenized)
        cmds = words_to_commands(sentenceStemmed)
    except Exception as e:
        print(str(e))


def words_to_commands(sentence):
    print("test")

