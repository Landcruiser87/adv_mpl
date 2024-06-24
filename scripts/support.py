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
    features_names = list
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
    # elif dataset_id == 45948:
    #     #If its the electric cars oneone.  Clean and load as such. 
    #     OpenDB.target = dataset["data"]["DEATH_EVENT"]
    #     OpenDB.data = dataset["data"].drop("DEATH_EVENT", axis=1) 
    #     OpenDB.data_description = dataset['DESCR']

    #     if 'target_names' in dataset.keys():
    #         if isinstance(dataset["target_names"], list):
    #             OpenDB.target_names = np.array(["living", "deceased"], dtype="U9")

    #     if 'feature_names' in dataset.keys():
    #         OpenDB.feature_names = list(dataset['feature_names'])
        
    #     OpenDB.rev_target_dict = {
    #         0:"living",
    #         1:"deceased"
    #     }
    return OpenDB

#old loader code
    # if url.endswith(".zip"):
    #     pass
    # elif url.endswith(".csv"):
    #     pass
    # elif url.endswith(""):
    # data = requests.get(url).content
    # df = pd.read_csv(io.StringIO(data.decode('utf-8')))

def sum_stats(datatype:str, title:str, data=pd.DataFrame):
    """Accepts a datatype you want to be summarized. 
    Manipulate the .agg function below to return your desired format.

    Args:
        stat_list (str): List of feature names
        title (str): What you want to call the plot
        data (pd.DataFrame) : The dataset you're working with
    """		
    #Add a rich table for results. 
    table = Table(title=title)
    table.add_column("Measure Name", style="green", justify="right")
    table.add_column("mean", style="sky_blue3", justify="center")
    table.add_column("std", style="turquoise2", justify="center")
    table.add_column("max", style="yellow", justify="center")
    table.add_column("min", style="gold3", justify="center")
    table.add_column("count", style="cyan", justify="center")

    #filter dataframe by types. 
    #options 
        # -To select all numeric types, use np.number or 'number'
        # -To select strings you must use the object dtype, but note that this will return all object dtype columns
        # -See the numpy dtype hierarchy
        # -To select datetimes, use np.datetime64, 'datetime' or 'datetime64'
        # -To select timedeltas, use np.timedelta64, 'timedelta' or 'timedelta64'
        # -To select Pandas categorical dtypes, use 'category'
        # -To select Pandas datetimetz dtypes, use 'datetimetz' or 'datetime64[ns, tz]'
    datacols = data.select_dtypes(include=datatype)
    for col in datacols:
        _mean, _stddev, _max, _min, _count = data[col].agg([np.mean, np.std, max, min, "count"]).T
        table.add_row(
            col,
            f"{_mean:.2f}",
            f"{_stddev:.2f}",
            f"{_max:.2f}",
            f"{_min:.2f}",
            f"{_count:.0f}",
        )
    console = Console()
    console.print(table)