import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer

def stemWords(wordList):
    ps = PorterStemmer()
    stemmedWords = []
    for w in wordList:
        stemmedWords.append(ps.stem(w))

    return stemmedWords




def process_sentence(sentence):
    try:
        sentenceWordsTokenized = word_tokenize(sentence)
        print(stemWords(sentenceWordsTokenized))
    except Exception as e:
        print(str(e))

<<<<<<< HEAD
=======


def words_to_commands(sentence):
    print("test")
>>>>>>> 76191b7c5bb58aca22e6d398fac046fad273b763
