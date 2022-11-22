import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing, metrics


class Utils:
    def __init__(self):
        self.X_encoder = preprocessing.OneHotEncoder(sparse=False)
        self.y_encoder = preprocessing.LabelEncoder()

    def load_df(self, path):
        header = ["buy_price", "maint", "num_doors", "num_persons", "lug_boot", "safety", "class"]
        df = pd.read_csv(path, header=None)
        df.columns = header
        return df

    def process_X(self, X, fit=True):
        if fit:
            X = self.X_encoder.fit_transform(X)
        else:
            X = self.X_encoder.transform(X)
        return X

    def define_train_test_split(self, df):
        # X is features, y is label
        X = df.drop(["buy_price", "num_persons"], axis=1)
        X = self.process_X(X)

        y = self.y_encoder.fit_transform(df[["buy_price"]])  # Transform to numerical labels

        X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.3)
        return X_train, X_test, y_train, y_test

    def evaluate_model(self, model, X_test, y_test):
        y_pred = model.predict(X_test)
        accuracy = metrics.accuracy_score(y_test, y_pred)  # tp / total
        precision = metrics.precision_score(y_test, y_pred, average='weighted')  # tp / (tp + fp)
        recall = metrics.recall_score(y_test, y_pred, average='weighted')  # tp / (tp + fn)
        print(f'Accuracy {accuracy}, Precision {precision}, Recall {recall}')
