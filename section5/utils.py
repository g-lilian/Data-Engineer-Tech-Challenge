import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing, metrics


class Utils:
    def __init__(self):
        # Specify order of categories
        self.categories = [['low', 'med', 'high', 'vhigh'],
                           ['2', '3', '4', '5more'],
                           ['small', 'med', 'big'],
                           ['low', 'med', 'high'],
                           ['unacc', 'acc', 'good', 'vgood']]
        self.X_encoder = preprocessing.OrdinalEncoder(categories=self.categories)
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

    def evaluate_model(self, model, X, y):
        y_pred = model.predict(X)
        accuracy = metrics.accuracy_score(y, y_pred)  # tp / total
        precision = metrics.precision_score(y, y_pred, average='weighted')  # tp / (tp + fp)
        recall = metrics.recall_score(y, y_pred, average='weighted')  # tp / (tp + fn)

        print(f'Accuracy {accuracy}, Precision {precision}, Recall {recall}')
