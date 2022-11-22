from utils import Utils
from sklearn.neighbors import KNeighborsClassifier


def train():
    CARS_DATASET = "dataset/car.data"
    utils = Utils()
    dataset = utils.load_df(CARS_DATASET)
    X_train, X_test, y_train, y_test = utils.define_train_test_split(dataset)

    model_knn = KNeighborsClassifier(n_neighbors=10)
    model_knn.fit(X_train, y_train)
    utils.evaluate_model(model_knn, X_test, y_test)

    return model_knn, utils


if __name__ == '__main__':
    train()
