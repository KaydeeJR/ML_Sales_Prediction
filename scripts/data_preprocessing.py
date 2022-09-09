"""
This script reads a version of data from drive and preprocesses it for the ML model.
1) Converting non-numeric columns to numeric ones using One-hot encoding because there are few columns.
2) handling NaN values
3) generating new features from datetime column 
4) Data scaling using StandardScaler
"""
from datetime import datetime
import pandas as pd
import os
import holidays
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer 
from pyts.preprocessing import InterpolationImputer

# preprocessing actions
numeric_transformer = Pipeline(steps=[('imputer',InterpolationImputer(strategy='linear')),('scaler', StandardScaler())])
categorical_transformer = Pipeline(
    steps=[('imputer',SimpleImputer(strategy='most_frequent',fill_value='missing')),('onehot', OneHotEncoder(handle_unknown='ignore'))])


class DFExtractor():
    """
    class that extracts certain features for preprocessing
    """
    def __init__(self, dataframe) -> None:
        self.dataframe = dataframe

    def get_categorical_columns(self) -> list:
        return self.dataframe.select_dtypes(exclude=['int64', 'float64','datetime64']).columns

    def get_numeric_columns(self) -> list:
        return self.dataframe.drop("Store",axis=1).select_dtypes(exclude=['object','datetime64']).columns
    
    def convert_to_datetime(self, col_name)->None:
        self.dataframe[col_name]= pd.to_datetime(self.dataframe[col_name])

    def find_weekdays(self):
        return self.dataframe.loc[self.dataframe["DayOfWeek"]<=5]

    def find_weekends(self):
        return self.dataframe.loc[self.dataframe["DayOfWeek"]>5]
    
    def find_holidays(self):
        """
        find holidays in the US
        """
        holiday_dict = {}
        # number of years in dataset
        years_list = list(self.dataframe['Date'].dt.year.value_counts().index)
        # get unique dates in date column
        unique_dates = self.dataframe["Date"].dt.date.value_counts().index
        for y in range(len(years_list)):
            for k, v in holidays.US(years=years_list[y]).items(): # k = dates, v = holiday name
                if k in unique_dates:
                     holiday_dict[k] = v
        return holiday_dict
        
    def find_days_to_holiday(self):
        # TODO
        pass
    def find_days_after_holiday(self):
        # TODO
        pass
    def find_month_start_mid_end(self)->list:
        # TODO
        pass
    def get_DF(self)->pd.DataFrame:
        return self.dataframe

if __name__ == "__main__":
    file_path_to_merged_dataset = "\\merged_train_sales_store.csv"
    merged_DF = pd.read_csv(
        os.getcwd()+"\\data"+file_path_to_merged_dataset,index_col="Unnamed: 0", low_memory=False)
    extractor = DFExtractor(merged_DF)
    extractor.convert_to_datetime("Date")
    numeric_cols = extractor.get_numeric_columns()
    category_cols = extractor.get_categorical_columns()
    preprocessor = ColumnTransformer(transformers=[('num_trans',numeric_transformer,numeric_cols),('cat',categorical_transformer,category_cols)])
    preprocessor.fit(extractor.get_DF())
    pd.DataFrame(preprocessor.transform(extractor.get_DF())) # <- returns dataframe
