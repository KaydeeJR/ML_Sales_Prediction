import pandas as pd
import os
import sys
# Dataset access
my_path = "D:\\10XAcademy\\ML_Sales_Prediction"
os.chdir(my_path)
path_to_module = os.path.abspath(os.getcwd()+"\\data")
if path_to_module not in sys.path:
    sys.path.append(path_to_module)
file_path_to_train_set = "\\train.csv"
file_path_to_test_set = "\\test.csv"
file_path_to_store_dataset = "\\store.csv"
file_path_to_merged_dataset = "\\merged_train_sales_store.csv"

def read_csv_file(filePath:str)->pd.DataFrame:
    return pd.read_csv(filePath, low_memory=False)

def save_as_csv(dataframe, filePath:str):
    dataframe.to_csv(filePath)
    return filePath

def merge_two_dataframes(dataframe1, dataframe2)->pd.DataFrame:
    """
    This function accepts two dataframe as arguments
    left_index => take the index in the left column i.e dataframe1 as joint dataframe index
    right_on => take column or index in right dataframe i.e. dataframe2 to join on 
    """
    return pd.merge(dataframe1,dataframe2,left_index=True, right_on='Store').reset_index()

if __name__ == "__main__":
    """
    1) get dataframes from CSV files
    2) merge dataframes
    3) save merged dataframes to CSV files
    """
    save_as_csv(merge_two_dataframes(read_csv_file(os.getcwd()+"\\data"+file_path_to_store_dataset),read_csv_file(os.getcwd()+"\\data"+file_path_to_train_set)),os.getcwd()+"\\data"+file_path_to_merged_dataset)
