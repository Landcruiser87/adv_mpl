import requests
import numpy as np
import pandas as pd
from sklearn import datasets
import rich
from rich.console import Console
from rich.table import Table
from dataclasses import dataclass
from datetime import timedelta

@dataclass
class OpenDB():
    target = pd.Series
    data = pd.DataFrame
    data_description = str
    target_names = list,
    feature_names = list
    target_dict = dict

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
        
        OpenDB.target_dict = {
            0:"living",
            1:"deceased"
        }

    elif dataset_id == 43482:
        OpenDB.target = ""
        OpenDB.data = dataset["data"]
        OpenDB.data_description = dataset['DESCR']

        if 'target_names' in dataset.keys():
            if isinstance(dataset["target_names"], list):
                OpenDB.target_names = dataset["target_names"]

        if 'feature_names' in dataset.keys():
            OpenDB.feature_names = dataset['feature_names']

        #Data Cleaning        
        #transform  times into timedelta's
        time_cols = ["Swim", "Bike", "Run", "T1", "T2", "Overall"]
        for col in time_cols:
            OpenDB.data[col] = OpenDB.data[col].astype("timedelta64[s]")
            OpenDB.data[col] = OpenDB.data[col].apply(lambda x:x.total_seconds())

        text_cols = ["Name", "Country", "Gender", "Division", "Division_Rank", "Gender_Rank", "Overall_Rank"]
        for col in text_cols:
            OpenDB.data[col] = OpenDB.data[col].astype("str")
        
        #replace DNFs with np.nans and flip the dtype to int so we can sort. 
        # for col in text_cols[4:]:
        #     OpenDB.data[(OpenDB.data[col]=="DNS") | (OpenDB.data[col]=="DNF") | (OpenDB.data[col]=="DQ")] = np.nan
        #     OpenDB.data[col] = OpenDB.data[col].astype("float")

        OpenDB.target_dict = { 'DEU': 'Germany', 'USA': 'United States',
            'AUS': 'Australia', 'GBR': 'United Kingdom', 'NZL': 'New Zealand',
            'CHE': 'Switzerland', 'BEL': 'Belgium', 'AUT': 'Austria', 'DNK':
            'Denmark', 'FRA': 'France', 'CAN': 'Canada', 'UKR': 'Ukraine',
            'SVN': 'Slovenia', 'ARG': 'Argentina', 'ZAF': 'South Africa',
            'ESP': 'Spain', 'PRT': 'Portugal', 'BRA': 'Brazil', 'KAZ':
            'Kazakhstan', 'MEX': 'Mexico', 'ITA': 'Italy', 'NLD':
            'Netherlands', 'FIN': 'Finland', 'LUX': 'Luxembourg', 'SWE':
            'Sweden', 'CHN': 'China', 'COL': 'Colombia', 'CZE': 'Czech Republic',
            'RUS': 'Russia', 'PRY': 'Paraguay', 'GRC': 'Greece',
            'HUN': 'Hungary', 'NOR': 'Norway', 'PER': 'Peru', 'KOR': 'South Korea',
            'IRL': 'Ireland', 'CRI': 'Costa Rica', 'EST': 'Estonia',
            'JPN': 'Japan', 'ROU': 'Romania', 'ISR': 'Israel', 'VEN':
            'Venezuela', 'PAN': 'Panama', 'SVK': 'Slovakia', 'POL': 'Poland',
            'CHL': 'Chile', 'ISL': 'Iceland', 'AND': 'Andorra', 'GTM':
            'Guatemala', 'HKG': 'Hong Kong', 'IND': 'India', 'TUR': 'Turkey',
            'PHL': 'Philippines', 'SRB': 'Serbia', 'URY': 'Uruguay', 'ECU':
            'Ecuador', 'SGP': 'Singapore', 'BMU': 'Bermuda', 'LVA': 'Latvia',
            'TWN': 'Taiwan', 'MCO': 'Monaco', 'THA': 'Thailand', 'PNG': 'Papua New Guinea', 
            'MYS': 'Malaysia', 'HRV': 'Croatia', 'PRI': 'Puerto Rico', 
            'MAR': 'Morocco', 'LBN': 'Lebanon', 'IMN': 'Isle of Man',
            'SAU': 'Saudi Arabia', 'DOM': 'Dominican Republic', 'VNM':
            'Vietnam', 'BGR': 'Bulgaria' }

    return OpenDB

# ehhhh why is this function here. 
# def time_convert(wrk_time:str)->timedelta:
#     if wrk_time[0].isnumeric and wrk_time[-1].isnumeric():
#         times = wrk_time.split(":")
#         hour = times[0]
#         min = times[1]
#         sec = times[2]
#         return timedelta(hours=hour, minutes=min, seconds=sec)
#     else:
#         return np.nan

# def convert_2_timedelta(second_time:int)->int:
#     hours, remainder = divmod(second_time, 3600)
#     minutes, seconds = divmod(remainder, 60)
#     return timedelta(hours=hours, minutes=minutes, seconds=seconds)

def convert_time_format(seconds)->str:
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return f"{int(hour):02d}:{int(minutes):02d}:{int(seconds):02d}"

def view_allcols(df:pd.DataFrame)->list:
    """Here we make a list of a zipped object.  The contents being a range numbering the 
    amount of columns and the column names. 

    Args:
        df (pd.DataFrame): el dataframe

    Returns:
        header (list of tuples): [(column index, column name)]
    """

    header = [("col_idx", "col_name", "dtype")]
    header.extend(list(zip(range(df.shape[1]),df.columns.tolist(), df.dtypes)))
    header = [f"{str(idx):8s} {name:14s} {str(dtype):12s}" for idx, name, dtype in header]
    for row in header:
        print(row)

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