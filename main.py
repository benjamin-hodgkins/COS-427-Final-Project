import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

import numpy as np

def main():
    
    #Cleaning up and evening the data
    data = pd.read_csv("abstracts.txt", sep=",", names=("Abstract", "Disease"))
    filtered = data[(data.Disease == "Heart Disease") | (data.Disease == "Influenza")
                | (data.Disease == "Lung Cancer") | (data.Disease == "HIV")]
    
    #Making train/validation/test sets
    one = filtered[filtered.Disease == "Heart Disease"].iloc[:10000]
    one_train = one[:7000]
    one_val = one[7000:8500]
    one_test = one[8500:10000]
    
    two = filtered[filtered.Disease == "Influenza"].iloc[:10000]
    two_train = two[:7000]
    two_val = two[7000:8500]
    two_test = two[8500:10000]
    
    three = filtered[filtered.Disease == "Lung Cancer"].iloc[:10000]
    three_train = three[:7000]
    three_val = three[7000:8500]
    three_test = three[8500:10000]
    
    four = filtered[filtered.Disease == "HIV"].iloc[:10000]
    four_train = four[:7000]
    four_val = four[7000:8500]
    four_test = four[8500:10000]
    
    train = one_train.append(two_train).append(three_train).append(four_train)
    val = one_val.append(two_val).append(three_val).append(four_val)
    test = one_test.append(two_test).append(three_test).append(four_test)
    
    #Building the classifiers
    #Naives Bayes Classifier
    naive_bayes_clf = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', MultinomialNB()),
    ])
    naive_bayes_clf.fit(train["Abstract"], train["Disease"])
    predicted = naive_bayes_clf.predict(test["Abstract"])
    print("Naive Bayes results:")
    print("Accuracy: %.8f" % (accuracy_score(test["Disease"], predicted)))
    print("Precision: %.8f" % (precision_score(test["Disease"], predicted, average='macro')))
    print("Recall: %.8f" % (recall_score(test["Disease"], predicted, average='macro')))
    print("F1 Score: %.8f" % (f1_score(test["Disease"], predicted, average='macro')))
    
    #SVM Classifier
    svm_clf = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', SGDClassifier(loss='hinge', penalty='l2',
                          alpha=1e-3, random_state=42,
                          max_iter=5, tol=None)),
    ])
    
    svm_clf.fit(train["Abstract"], train["Disease"])
    predicted = svm_clf.predict(test["Abstract"])
    print("SVM results:")
    print("Accuracy: %.8f" % (accuracy_score(test["Disease"], predicted)))
    print("Precision: %.8f" % (precision_score(test["Disease"], predicted, average='macro')))
    print("Recall: %.8f" % (recall_score(test["Disease"], predicted, average='macro')))
    print("F1 Score: %.8f" % (f1_score(test["Disease"], predicted, average='macro')))
    
    #Logistic Regression Classifier
    logitic_regression_clf = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', LogisticRegression(solver='liblinear')),
    ])
    logitic_regression_clf.fit(train["Abstract"], train["Disease"])
    predicted = logitic_regression_clf.predict(test["Abstract"])
    print("Logisitic Regression results:")
    print("Accuracy: %.8f" % (accuracy_score(test["Disease"], predicted)))
    print("Precision: %.8f" % (precision_score(test["Disease"], predicted, average='macro')))
    print("Recall: %.8f" % (recall_score(test["Disease"], predicted, average='macro')))
    print("F1 Score: %.8f" % (f1_score(test["Disease"], predicted, average='macro')))
    
main()