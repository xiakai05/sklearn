# -*- encoding:utf-8 -*-
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from os import listdir
from os.path import isfile, join
import jieba
import os
import json
import codecs
from sklearn import metrics
from sklearn.externals import joblib
mypath=join(os.path.pardir,'data')
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
dataset_X=[]
dataset_Y=[]
stopwords=json.load(open('../'+'stopwords.json'))

for filename in onlyfiles:
    with codecs.open(mypath+'/'+filename, encoding='utf-8') as file :
        for line in file:
            dataset_X.append(' '.join(jieba.cut(line.strip())))
            dataset_Y.append(filename)

X_train, X_test, y_train, y_test = train_test_split(dataset_X, dataset_Y, test_size=0.33, random_state=42)
text_clf = Pipeline([('vect', CountVectorizer()),
                     ('clf', LogisticRegression())])

text_clf = text_clf.fit(X_train, y_train)
predicted = text_clf.predict(X_test)
print(metrics.classification_report(y_test, predicted))
joblib.dump(text_clf,'../model/chat_clf.pkl')
useful=open('../result/useful.txt','w')
unuseful=open('../result/unuseful.txt','w')
for content in X_test:
    res = text_clf.predict([content])
    if res == 'qf_useful.txt':
        useful.write(content.replace(' ','').encode('utf8') + '\n')
    else:
        unuseful.write(content.replace(' ','').encode('utf8') + '\n')

from sklearn.externals import joblib

joblib.dump(text_clf,'../model/chat_clf.pkl')