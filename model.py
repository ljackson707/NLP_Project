from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

#------------------------------------------------------------------------------------------------------------------------------------------------------

# We'll use this split function later to create in-sample and out-of-sample datasets for modeling
def split(df, stratify_by=None):
    """
    3 way split for train, validate, and test datasets
    To stratify, send in a column name
    """
    
    train, test = train_test_split(df, test_size=.2, random_state=123, stratify=df[stratify_by])
    
    train, validate = train_test_split(train, test_size=.3, random_state=123, stratify=train[stratify_by])
    
    return train, validate, test

#------------------------------------------------------------------------------------------------------------------------------------------------------

def Model(X_train_vectorized, X_validate_vectorized, X_test_vectorized, y_train, y_validate, y_test):
    
    # Now you have a vactorized dataset and its fit on the clasification model.

    lm = DecisionTreeClassifier().fit(X_train_vectorized, y_train)

    train = pd.DataFrame(dict(actual=y_train))
    validate = pd.DataFrame(dict(actual=y_validate))
    test = pd.DataFrame(dict(actual=y_test))
    
    train['predicted'] = lm.predict(X_train_vectorized)
    validate["predicted"] = lm.predict(X_validate_vectorized)
    test['predicted'] = lm.predict(X_test_vectorized)
    
    # Train Accuracy
    aT = (train.actual == train.predicted).mean()
    
    aV = (validate.actual == validate.predicted).mean()
    
    return aT, aV

#------------------------------------------------------------------------------------------------------------------------------------------------------