#!/usr/bin/env python
# coding: utf-8

from sklearn.externals import joblib
import numpy as np
from sklearn import preprocessing
from sklearn.feature_extraction.text import TfidfVectorizer

# In[5]:
def extract_and_get_intent(message):
    with open('saved_model_tfidf_linearSVC_v2.pkl', 'rb') as file:
        tfidf_svc_clf = joblib.load(file)
    with open('vectorizer_for_tfidf_linearSVC_v2.pkl', 'rb') as file:
        vectorizer = joblib.load(file)
    X=vectorizer.transform([message])
    X = X.todense()
    pred_result =tfidf_svc_clf.predict(X)
    list_label=['contact','register','activity','work','joiner']
    le = preprocessing.LabelEncoder()
    le.fit_transform(list_label)
    return str(le.inverse_transform(pred_result)[0])



# In[24]:

if __name__ == '__main__':
    result=extract_and_get_intent("đi hoạt động này làm gì vậy ?")
    print("------------extract raw")
    print(result)






# In[ ]:




