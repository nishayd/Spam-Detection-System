from joblib import dump, load

def save_model(clf, filename):
    dump(clf, filename)

def load_model(filename):
    return load(filename)

def make_prediction(messages):
    clf = load_model('static/spam_classifier.joblib')
    outputs = []
    for message in messages:
        result = clf.predict([message])[0]
        if result == 0:
            outputs.append({
                'message': message,
                'label': 'Not Spam',
                'value': 0,
            })
        else:
            outputs.append({
                'message': message,
                'label': 'Spam',
                'value': 1,
            })
    return outputs