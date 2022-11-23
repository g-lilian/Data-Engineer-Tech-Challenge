from utils import Utils
import matplotlib.pyplot as plt


# Add a new col with value 1 if the existing value matches the specified category, and 0 otherwise
def add_category_counts(df, feat, category):
    col_name = feat + "_" + category
    df[col_name] = df.apply(lambda row: 1 if row[feat] == category else 0, axis=1)
    return df


def show_feature_occurrences(utils):
    df = utils.load_df("dataset/car.data")
    header = ["buy_price", "maint", "num_doors", "num_persons", "lug_boot", "safety", "class"]

    # for category in ["low", "med", "high", "vhigh"]:
    #     add_category_counts(df, "maint", category)
    # for category in ["2", "3", "4", "5more"]:
    #     add_category_counts(df, "num_doors", category)
    for category in ["unacc", "acc", "good", "vgood"]:
        add_category_counts(df, "class", category)

    grouped_by_price_df = df.groupby(["buy_price"]).sum().reset_index()

    fig, ax = plt.subplots()
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')
    table = ax.table(cellText=grouped_by_price_df.values, colLabels=grouped_by_price_df.columns, loc='center')
    table.scale(1.2, 2)
    plt.gcf().set_size_inches(12, 3)

    plt.savefig('feature_counts_2.png', bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    utils = Utils()
    show_feature_occurrences(utils)
