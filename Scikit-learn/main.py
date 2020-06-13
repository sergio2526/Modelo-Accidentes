from utils import Utils
from models import Models

if __name__ == "__main__":

    utils = Utils()
    models = Models()

    data = utils.load_from_csv('./data/X.csv')
    X, y = utils.features_target(data,['RADICADO','DIA_NUMERO','PERIODO','CBML','MES','NUM_COMUNA'],['DIA'])

    models.grid_training(X,y)

    print(data)
