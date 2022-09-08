import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
import data_extraction
# preprocessing actions
numeric_transformer = Pipeline(steps=[('scaler', StandardScaler())])
categorical_transformer = Pipeline(
    steps=[('onehot', OneHotEncoder(handle_unknown='ignore'))])


class DFExtractor():
    def __init__(self, dataframe) -> None:
        self.dataframe = dataframe

    def get_numeric_columns(self) -> list:
        return self.dataframe.select_dtypes(include=['int64', 'float64']).columns

    def get_categorical_columns(self, dataframe) -> list:
        return self.dataframe.select_dtypes(include=['object']).columns


if __name__ == "__main__":
    extractor = DFExtractor(pd.read_csv(
        os.getcwd()+"\\data"+file_path_to_train_set, low_memory=False))
    print(extractor.get_numeric_columns())
    #preprocessor = ColumnTransformer(transformers=[()])
