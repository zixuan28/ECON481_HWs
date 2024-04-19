#Ex 0:
def github() -> str:
    """
   This code would give you a link to my GitHub Repository page!
    """

    return "https://github.com/zixuan28/ECON481_HWs/blob/main/481HW4.py"

#Ex 1:
import pandas as pd

def load_data() -> pd.DataFrame:
    """
    The function reads in the data from the link.
    """
    data = pd.read_csv("https://lukashager.netlify.app/econ-481/data/TSLA.csv")

    return data

#Ex 2:
import matplotlib.pyplot as plt

def plot_close(df: pd.DataFrame, start: str = '2010-06-29', end: str = '2024-04-15') -> None:
    """
    The function first converts the Date column into datetime object and sets it as the index.
    Then, the function take the dataframe from the starting date to the ending date.
    The function then plot the closing price of TSLA from the starting date to the ending date.
    """
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df = df.loc[start:end]

    plt.plot(df.index, df['Close'])
    plt.title(f"TSLA Closing Price from {start} to {end}")
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.show()

#Ex 3:
