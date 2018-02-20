from nltk.corpus import conll2002
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import Perceptron
from sklearn.metrics import precision_recall_fscore_support

# Assignment 6: NER
# This is just to help you get going. Feel free to
# add to or modify any part of it.


def getfeats(word, o):
    """ This takes the word in question and
    the offset with respect to the instance
    word (usually between [-2,2]) """
    o = str(o)
    features = [
        (o + 'word', word)
        # TODO: add more features here.
    ]
    return features
    

def word2features(sent, i):
    """ The function generates all features
    for the word at position i in the
    sentence."""
    features = []
    # the window around the token
    for o in [-2,0,2]:
        if i+o >= 0 and i+o < len(sent):
            word = sent[i+o][0]
            featlist = getfeats(word, o)
            features.extend(featlist)
    
    return dict(features)

if __name__ == "__main__":
    # Load the training data
    train_sents = list(conll2002.iob_sents('esp.train'))
    dev_sents = list(conll2002.iob_sents('esp.testa'))
    test_sents = list(conll2002.iob_sents('esp.testb'))
    
    train_feats = []
    train_labels = []

    for sent in train_sents:
        for i in range(len(sent)):
            feats = word2features(sent,i)
            train_feats.append(feats)
            train_labels.append(sent[i][-1])

    vectorizer = DictVectorizer()
    X_train = vectorizer.fit_transform(train_feats)

    # TODO: play with other models
    model = Perceptron(verbose=1)
    model.fit(X_train, train_labels)

    test_feats = []
    test_labels = []
    
    for sent in test_sents:
        for i in range(len(sent)):
            feats = word2features(sent,i)
            test_feats.append(feats)
            test_labels.append(sent[i][-1])

    X_test = vectorizer.transform(test_feats)
    y_pred = model.predict(X_test)

    j = 0
    print("Writing to results.txt")
    # format is: word gold pred
    with open("results.txt", "w") as out:
        for sent in test_sents: 
            for i in range(len(sent)):
                word = sent[i][0]
                gold = sent[i][-1]
                pred = y_pred[j]
                j += 1
                out.write("{}\t{}\t{}\n".format(word,gold,pred))
        out.write("\n")
    


    # We don't care about score on the O label. It's always very high.
    #labels = set(test_labels)
    #labels.remove("O")
    #labels = sorted(list(labels))

    #p,r,f1,support = precision_recall_fscore_support(test_labels, y_pred, labels=labels)

    #print("Scores\tPrecision\tRecall\tF1")
    #for tt in zip(labels,p,r,f1):
    #    print("{}\t{}\t{}\t{}".format(tt[0], tt[1], tt[2], tt[3]))
    #print("-------------------")
    #p,r,f1,support = precision_recall_fscore_support(test_labels, y_pred, labels=list(labels), average="micro")
    #print("Overall\t{}\t{}\t{}".format(p,r,f1)) 






