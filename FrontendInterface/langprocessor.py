import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer

def stemWords(wordList):
    ps = PorterStemmer()
    stemmedWords = []
    for w in wordList:
        stemmedWords.append(ps.stem(w))

    return stemmedWords

def intersect(a, b):
    return list(set(a) & set(b))

def words_to_commands(sentence):

    cmd_dict = {
        "state" : True,
        "subject" : None,
        "searchterms": None
    }

    list_subject = ["lamp","light","bulb"]
    list_state = ["off", "on"]
    print(sentence)
    cmd_dict["subject"]=intersect(list_subject, sentence)
    cmd_dict["state"]=intersect(list_state, sentence)

    return cmd_dict

def process_sentence(sentence):
    try:
        sentenceWordsTokenized = word_tokenize(sentence)
        sentenceStemmed = stemWords(sentenceWordsTokenized)
        cmds = words_to_commands(sentenceStemmed)
        print(cmds)
    except Exception as e:
        print(str(e))
<<<<<<< HEAD


def words_to_commands(sentence):
    print("test")

=======
>>>>>>> 6946a2b350c063d7f8572b07023b76cd7a92c159
