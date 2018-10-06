import recognize
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
nltk.download('punkt')
porterStemmer = PorterStemmer()

request_input = recognize.create_instance()

words = word_tokenize(request_input["transcription"])

print(words)