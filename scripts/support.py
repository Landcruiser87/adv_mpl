import requests
import numpy as np
import pandas as pd
import io
from sklearn import datasets
import rich
from rich.console import Console
from rich.table import Table
from dataclasses import dataclass


@dataclass
class OpenDB():
    target = pd.Series
    data = pd.DataFrame
    data_description = str
    target_names = list,
    feature_names = list
    rev_target_dict = dict

def grab_dataset(dataset_id:int):
    #use openml to pull in the dataset
    dataset = datasets.fetch_openml(
        data_id=dataset_id,  
        return_X_y=False,
        as_frame=True,
        parser="auto"
    )
    
    if dataset_id == 43008:
        #If its the UCI heart one.  Clean and load as such. 
        OpenDB.target = dataset["data"]["DEATH_EVENT"]
        OpenDB.data = dataset["data"].drop("DEATH_EVENT", axis=1) 
        OpenDB.data_description = dataset['DESCR']

        if 'target_names' in dataset.keys():
            if isinstance(dataset["target_names"], list):
                OpenDB.target_names = np.array(["living", "deceased"], dtype="U9")

        if 'feature_names' in dataset.keys():
            OpenDB.feature_names = list(dataset['feature_names'])
        
        OpenDB.rev_target_dict = {
            0:"living",
            1:"deceased"
        }
    elif dataset_id == 45103:
        OpenDB.target = dataset["target"]
        OpenDB.data = dataset["data"]
        OpenDB.data_description = dataset['DESCR']

        if 'target_names' in dataset.keys():
            if isinstance(dataset["target_names"], list):
                OpenDB.target_names = dataset["target_names"]

        if 'feature_names' in dataset.keys():
            OpenDB.feature_names = dataset['feature_names']
        
        OpenDB.rev_target_dict = {}


    return OpenDB

def sum_stats(datatype:str, title:str, data=pd.DataFrame):
    """Accepts a datatype you want to be summarized. 
    Manipulate the .agg function below to return your desired format.

    Args:
        datatype (str): what type of data you want selected for the table
        title (str): What you want to call the table
        data (pd.DataFrame) : The dataset you're working with
    """		
    #filter dataframe by types. 
    #options from pandas docs
        # -To select all numeric types, use np.number or 'number'
        # -To select strings you must use the object dtype, but note that this will return all object dtype columns
        # -See the numpy dtype hierarchy
        # -To select datetimes, use np.datetime64, 'datetime' or 'datetime64'
        # -To select timedeltas, use np.timedelta64, 'timedelta' or 'timedelta64'
        # -To select Pandas categorical dtypes, use 'category'
        # -To select Pandas datetimetz dtypes, use 'datetimetz' or 'datetime64[ns, tz]'

    #Add a rich table for results. 
    table = Table(title=title)
    table.add_column("Idx", style="sky_blue3", justify="center")
    table.add_column("Measure Name", style="green", justify="left")
    table.add_column("Mean", style="sky_blue3", justify="center")
    table.add_column("Std", style="turquoise2", justify="center")
    table.add_column("Min", style="gold3", justify="center")
    table.add_column("Max", style="yellow", justify="center")
    table.add_column("Count", style="cyan", justify="center")


        
    datacols = data.select_dtypes(include=datatype)
    colnames = data.columns.tolist()
    for col in datacols:
        _mean, _stddev, _max, _min, _count = data[col].agg([np.mean, np.std, max, min, "count"]).T
        table.add_row(
            f"{colnames.index(col):d}",
            col,
            f"{_mean:.1f}",
            f"{_stddev:.1f}",
            f"{_min:.1f}",
            f"{_max:.1f}",
            f"{_count:.0f}",
        )
    console = Console()
    console.print(table)
    
def view_allcols(df:pd.DataFrame)->list:
    """Here we make a list of a zipped object.  The contents being a range numbering the 
    amount of columns and the column names. 

    Args:
        df (pd.DataFrame): el dataframe

    Returns:
        header (list of tuples): [(column index, column name)]
    """
    header = [("col_idx", "col_name")]
    header.extend(list(zip(range(df.shape[1]),df.columns.tolist())))
    return header