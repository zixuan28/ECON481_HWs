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
    