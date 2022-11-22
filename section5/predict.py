from train import train
import pandas as pd


def predict(model, utils):
    header = ["maint", "num_doors", "lug_boot", "safety", "class"]
    input_X = pd.DataFrame([['high', '4', 'big', 'high', 'good'],
                            ['vhigh', '2', 'big', 'low', 'vgood'],
                            ['med', '3', 'med', 'med', 'acc'],
                            ['low', '5more', 'small', 'high', 'unacc']], columns=header)
    input_X = utils.process_X(input_X, fit=False)
    pred_y = model.predict(input_X)
    pred_y = utils.y_encoder.inverse_transform(pred_y)

    # print(pred_y)
    print(f"The predicted buying price is {pred_y[0]}.")


if __name__ == '__main__':
    model, utils = train()
    predict(model, utils)
