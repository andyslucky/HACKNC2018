import input_io
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
nltk.download('punkt')
porterStemmer = PorterStemmer()

request_input = input_io.create_instance()

words = word_tokenize(request_input["transcription"])

print(words)