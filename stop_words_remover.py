import sys,os
import  pandas as pd
import nltk
from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
#инициализируем стоп слова и символы
stop = set(stopwords.words('russian'))
stop.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}','#','№'])

def remove_stop_words(query):
    str = ''
    for i in wordpunct_tokenize(query):
        if i not in stop and not i.isdigit():
            str = str + i + ' '

    return str

def clean_csv(df):
    for index,row in df.iterrows():
        row['запрос'] = remove_stop_words(row['запрос']).rstrip().lower()


print(remove_stop_words("ну я как бы говорю тебе об этом"))
