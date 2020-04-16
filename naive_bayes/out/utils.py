
import pandas as pd

class Utils:

    def load_set(self,path):

        return pd.read_csv(path, sep='delimiter', encoding = 'utf8' )


    def data_export(self,dataset,path):

        y = dataset.to_csv(path, index = False)

        return y



