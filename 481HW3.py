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
import pyxlsb as px

def import_parent_companies(years: list) -> pd.DataFrame:
    url_parent = "https://lukashager.netlify.app/econ-481/data/ghgp_data_parent_company_09_2023.xlsb"
    
    dfs = [
        pd.read_excel(url_parent, sheet_name=str(year)).assign(year=year)
        for year in years
    ]
    
    concat_data = pd.concat(dfs, ignore_index=True)
    concat_data.dropna(how='all', inplace=True)
    
    return concat_data
