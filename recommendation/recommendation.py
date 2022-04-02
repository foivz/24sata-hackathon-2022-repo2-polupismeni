# import the necessary python libraries
import pandas as pd
from apyori import apriori


def find_recommended_things(item):
    # importing the dataset, consider the header as it contains products
    # https://www.kaggle.com/datasets/hemanthkumar05/market-basket-optimization
    dataset = pd.read_csv('/home/piki/PycharmProjects/24sata-hackathon-2022-repo2-polupismeni/recommendation/Market_Basket_Optimisation.csv', header=None, index_col=False)
    dataset = dataset.fillna(0)  # Fill 0 in place of nan values

    # creating a list of transactions
    transactions = []
    for i in range(0, 7501):
        transactions.append([str(dataset.values[i, j]) for j in range(0, 20) if str(dataset.values[i, j]) != '0'])

    # create an object of apriori function and set the threshold values for metrics
    rules = apriori(transactions, min_support=0.003, min_confidence=0.2, min_lift=3, min_length=2)
    rules_list = list(rules)
    #print(rules_list)
    # converting the list to a dataframe
    result = pd.DataFrame(rules_list)

    # save support to a separate column
    support = result.support

    # all four empty lists will contain the items, confidence and lift respectively.
    item1 = []
    item2 = []
    confidence = []
    lift = []

    # first and second item are frozensets and it has to be converted to a list
    for i in range(result.shape[0]):
        list1 = result['ordered_statistics'][i][0]
        item1.append(list(list1[0]))
        item2.append(list(list1[1]))
        confidence.append(list1[2])
        lift.append(list1[3])

    # convert the lists to dataframe
    item_1 = pd.DataFrame(item1)
    item_2 = pd.DataFrame(item2)
    conf = pd.DataFrame(confidence, columns=['Confidence'])
    lift_m = pd.DataFrame(lift, columns=['Lift'])

    # concatenate the individual dataframes to a single dataframe
    final_result = pd.concat([item_1, item_2, support, conf, lift_m], axis=1)

    # fill the missing values
    final_result = final_result.fillna(value=' ')

    # rename the columns
    final_result.columns = ['Item1', 'Item2', 'Item3', 'Item4', 'Item5', 'Support', 'Confidence', 'Lift']

    return_df = final_result[final_result['Item1'] == item]
    return_df = filter(None, return_df[['Item2', 'Item3', 'Item4', 'Item5']].values.tolist())
    return_df = [item for sublist in return_df for item in sublist if item != ""]
    return_df = [i for i in return_df if i]
    return list(return_df)


if __name__ == '__main__':
    find_recommended_things("pasta")
