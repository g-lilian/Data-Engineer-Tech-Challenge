from utils import Utils
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm


def train():
    CARS_DATASET = "dataset/car.data"
    utils = Utils()
    dataset = utils.load_df(CARS_DATASET)
    X_train, X_test, y_train, y_test = utils.define_train_test_split(dataset)

    # model = KNeighborsClassifier(n_neighbors=10)
    # model = RandomForestClassifier(n_estimators=100)
    # model = svm.SVC()
    model = DecisionTreeClassifier(criterion='gini', max_depth=2, random_state=42)
    model.fit(X_train, y_train)

    print("Train accuracy:")
    utils.evaluate_model(model, X_train, y_train)

    print("Test accuracy:")
    utils.evaluate_model(model, X_test, y_test)

    return model, utils


if __name__ == '__main__':
    train()
