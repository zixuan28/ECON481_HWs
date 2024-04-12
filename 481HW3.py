import pandas as pd

#Ex 0:
def github() -> str:
    """
   This code would give you a link to my GitHub Repository page!
    """

    return "https://github.com/zixuan28/ECON481_HWs/blob/main/481HW3.py"

#Ex 1:
def import_yearly_data(years: list) -> pd.DataFrame:
    links = {
        2022: "https://lukashager.netlify.app/econ-481/data/ghgp_data_2022.xlsx",
        2021: "https://lukashager.netlify.app/econ-481/data/ghgp_data_2021.xlsx",
        2020: "https://lukashager.netlify.app/econ-481/data/ghgp_data_2020.xlsx",
        2019: "https://lukashager.netlify.app/econ-481/data/ghgp_data_2019.xlsx"
    }
    
    data_frames = [
        pd.read_excel(links[year], sheet_name='Direct Emitters', skiprows=3).assign(year=year)
        for year in years if year in links
    ]

    concat_data = pd.concat(data_frames, ignore_index = True)
    
    return concat_data