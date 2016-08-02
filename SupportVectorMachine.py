import nltk.classify
from sklearn.svm import LinearSVC

classifier = nltk.classify.SklearnClassifier(LinearSVC())
classifier.train(train_features)

for test_record in test_data_list:
    features = extract_features(test_record)
    predict = classifier.classify(features)
    print predict