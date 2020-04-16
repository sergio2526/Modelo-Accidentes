
from utils import Utils
from naive_bayes import Model


if __name__ == '__main__':

    model = Model()

    df = model.dataset()

    print(df)
