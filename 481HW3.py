#Ex 0:
def github() -> str:
    """
   This code would give you a link to my GitHub Repository page!
    """

    return "https://github.com/zixuan28/ECON481_HWs/blob/main/481HW3.py"

#Ex 1:
import pandas as pd

def import_yearly_data(years: list) -> pd.DataFrame:
    '''
    This function takes a list of years and returns a dataframe with the data from the years in the list.
    The function first take all the years in the list and check if the year is in the links dictionary.
    If the year is in the links dictionary, the function reads the data from the link and assigns the year to the data.
    The function then concatenates the dataframes without the original indices from the sets.
    '''
    links = {
        2022: "https://lukashager.netlify.app/econ-481/data/ghgp_data_2022.xlsx",
        2021: "https://lukashager.netlify.app/econ-481/data/ghgp_data_2021.xlsx",
        2020: "https://lukashager.netlify.app/econ-481/data/ghgp_data_2020.xlsx",
        2019: "https://lukashager.netlify.app/econ-481/data/ghgp_data_2019.xlsx"
    }
    
    data_frames = [
        pd.read_excel(links[year], sheet_name='Direct Emitters', skiprows=3).assign(year=year) #reading data with year in the link
        for year in years if year in links #making sure the year is in the links
    ]

    concat_data = pd.concat(data_frames, ignore_index = True) #concatenating the dataframes without the original indices from the sets
    
    return concat_data

#Ex 2:
import pandas as pd

def import_parent_companies(years: list) -> pd.DataFrame:
    '''
    This function takes a list of years and returns a dataframe with the data from the years in the list.
    The function first takes all the years in the list and reads the data from the link with the year in the link.
    The function then concatenates the dataframes without the original indices from the sets.
    '''
    url_parent = "https://lukashager.netlify.app/econ-481/data/ghgp_data_parent_company_09_2023.xlsb"
    
    dfs = [
        pd.read_excel(url_parent, sheet_name=str(year)).assign(year=year)
        for year in years
    ]
    
    concat_data = pd.concat(dfs, ignore_index=True)
    concat_data.dropna(how='all', inplace=True)
    
    return concat_data

#Ex 3:
def n_null(df: pd.DataFrame, col: str) -> int:
    """
    This function takes a dataframe and a column name and returns the number of missing values in the column.
    """

    return pd.isnull(df[col]).sum()

#Ex 4:
import pandas as pd

def clean_data(emissions_data: pd.DataFrame, parent_data: pd.DataFrame) -> pd.DataFrame:
    """
    This function takes two dataframes and returns a cleaned dataframe.
    The function first renames the columns of the dataframes to make the merging easier.
    The function then merges the dataframes on the year and Facility ID columns.
    The function then selects the columns that we want to keep in the final dataframe.
    The function then renames the columns to lowercase.
    """
    parent_data.rename(columns={'GHGRP FACILITY ID': 'Facility ID'}, inplace=True)
    emissions_data.rename(columns={'Facility Id': 'Facility ID'}, inplace=True)
    
    merged_data = pd.merge(parent_data, emissions_data, how='left', on = ['year', 'Facility ID'])
    
    final_data = merged_data[
    [
    'Facility ID', 'year', 'State', 'Industry Type (sectors)', 'Total reported direct emissions', 
    'PARENT CO. STATE', 'PARENT CO. PERCENT OWNERSHIP'
    ]
    ]
    
    final_data.columns = final_data.columns.str.lower()
    
    return final_data

#Ex 5:
import pandas as pd

def aggregate_emissions(df: pd.DataFrame, group_vars: list) -> pd.DataFrame:
    """
    This function takes a dataframe and a list of group variables and returns an aggregated dataframe.
    The function groups the data by the group variables and calculates the minimum, median, mean, and maximum of the total reported direct emissions and parent co. percent ownership.
    The function then sorts the data by the mean of the total reported direct emissions in descending order.
    """
    agg_dict = {
        'total reported direct emissions': ['min', 'median', 'mean', 'max'],
        'parent co. percent ownership': ['min', 'median', 'mean', 'max']
    }

    agg_data = df.groupby(group_vars, as_index=True).agg(agg_dict)

    agg_data.sort_values(by=('total reported direct emissions', 'mean'), ascending=False, inplace=True)

    return agg_data
    