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
    
    doublestatechanged = False
    state_changed = False

    cmd_dict = {
        "state": True,
        "subject": None,
        "searchterms": None,
        "error": None
    }

    list_subject = ["lamp", "light", "bulb"]
    list_state = ["on", "off"]
    #Debug
    print(sentence)

    cmd_dict["subject"] = intersect(list_subject, sentence)
    cmd_dict["state"] = intersect(list_state, sentence)

    if len(cmd_dict.get("state")) > 1:
        cmd_dict["error"] = "Multiple States Entered"
    elif len(cmd_dict.get("state")) == 0:
        cmd_dict["error"] = "No State Entered"

    # print(cmd_dict)

    return cmd_dict

def process_sentence(sentence: object) -> object:
    try:
        sentence_words_tokenized = word_tokenize(sentence)
        sentence_stemmed = stemWords(sentence_words_tokenized)
        cmds = words_to_commands(sentence_stemmed)
        return cmds
    except Exception as e:
        print(str(e))

