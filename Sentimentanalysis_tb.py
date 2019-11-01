import nltk
from textblob import TextBlob

blob1 = TextBlob('I hate my office')

print(format(blob1.sentiment))
