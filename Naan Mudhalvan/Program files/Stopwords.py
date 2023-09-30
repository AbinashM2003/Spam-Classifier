import nltk
nltk.download('stopwords')
#remove the punctuations and stopwords
import string
def text_process(text):
text = text.translate(str.maketrans('', '', string.punctuation))
text = [word for word in text.split() if word.lower() not in stopwords.words('english')]
return " ".join(text)
data['text'] = data['text'].apply(text_process)
data.head()