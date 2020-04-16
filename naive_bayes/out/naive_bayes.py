import pandas as pd
from utils import Utils
from sklearn.naive_bayes import GaussianNB


class Model:

    def dataset(self):

        utils = Utils()

        dataset = utils.load_set("../in/Accidentalidad.csv")

        train= dataset.sample(frac = 0.6, random_state = 1)
        test = dataset.sample(frac = 0.4, random_state = 1)

        utils.data_export(train,"../in/train.csv")
        utils.data_export(test,'../in/test.csv')

        test = test.drop(['GRAVEDAD'], axis =1)

        return test

        



