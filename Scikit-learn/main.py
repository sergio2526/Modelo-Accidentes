from utils import Utils
from models import Models

if __name__ == '__main__':

    utils = Utils()
    models = Models()

    data = utils.load_from_csv('./data/X.csv')
    X, y = utils.features_target(data,['X','Y','OBJECTID','RADICADO','DIA_NUMERO','PERIODO','CBML','MES','DIA','NUM_COMUNA'],['DIA'])

    models.grid_training(X,y)

    print(data)
