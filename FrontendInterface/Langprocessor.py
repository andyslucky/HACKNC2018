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
        "state": True,
        "subject": None,
        "searchterms": None,
        "error": None
    }

    list_subject = ["lamp", "light", "bulb"]
    list_state = ["on", "off"]
    #Debug
    print("Sentence: " + str(sentence))

    cmd_dict["subject"] = intersect(list_subject, sentence)
    cmd_dict["state"] = intersect(list_state, sentence)

    # input error if more than one input for state
    if len(cmd_dict.get("state")) > 1:
        cmd_dict["error"] = "Multiple States Entered"
    elif len(cmd_dict.get("state")) == 0:
        cmd_dict["error"] = "No State Entered"

    #if we say 'on' without a subject keyword (referring to our light), give error.
    if cmd_dict.get("subject") is None:
        cmd_dict["error"] = "No subject."

    print("DEBUG: cmd_dict is " + str(cmd_dict))

    # print(cmd_dict)

    return cmd_dict

def cmd_parse(cmd_dict):
    # Rename off to false and on to true, provided they are the only entry for state.
    if cmd_dict.get("state") is "off":
        cmd_dict["state"] = False
        print("state \"off\" renamed to \"false\" " + cmd_dict.get("state"))
    elif cmd_dict.get("state") is "on":
        cmd_dict["state"] = True
        print("state \"on\" renamed to \"true\" " + cmd_dict.get("state"))

    #If there are any errors, state will be None.
    if cmd_dict.get("error") is not None:
        cmd_dict["state"]=None


    print("DEBUG: State Value is " + str(cmd_dict.get("state")))

    if cmd_dict.get("state") is None:
        return None
    else:
        return 1 if cmd_dict.get("state") else 0



def process_sentence(sentence: object) -> object:
    try:
        sentence_words_tokenized = word_tokenize(sentence)
        sentence_stemmed = stemWords(sentence_words_tokenized)
        cmds = words_to_commands(sentence_stemmed)
        input = cmd_parse(cmds)
        return input
    except Exception as e:
        print(str(e))


