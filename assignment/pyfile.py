import pandas as pd
file = open('Beyond the Wall of Sleep.txt', encoding="utf8")
Beyond= file.read()
file2 = open('Pride and Prejudice.txt', encoding="utf8")
Pride= file2.read()
Beyond=Beyond.lower().split()
Pride=Pride.lower().split()
intersection = set(Beyond) & set(Pride)
import string
table = str.maketrans('', '', string.punctuation)
intersection = [w.translate(table) for w in intersection]
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = stopwords.words('english')

intersection = [w for w in intersection if not w in stop_words]

intersection = list(set(intersection))
print(len(intersection))
print(intersection)