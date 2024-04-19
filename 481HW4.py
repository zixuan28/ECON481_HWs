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
import pandas as pd

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
import statsmodels.api as sm
import pandas as pd

def autoregress(df: pd.DataFrame) -> float:
    """
    The function first creates a new column 'delta_close' which is the difference between the closing price of the current day and the previous day.
    Then, the function creates another column 'delta_close_old' which is the 'delta_close' column shifted up by 1.
    Then, the function drops all na values.
    The function then creates two variables Delta_X and Delta_X_old.
    The function then runs an OLS regression of Delta_X on Delta_X_old without an intercept and uses HC1 hetroscedasticity robust standard errors.
    """
    df['delta_close'] = df['Close'].diff()
    df['delta_close_old'] = df['delta_close'].shift(1)
    df = df.dropna()
    Delta_X = df['delta_close']
    Delta_X_old = df['delta_close_old']
    model3 = sm.OLS(Delta_X, Delta_X_old).fit(cov_type='HC1')
    
    return model3.tvalues[0]

#Ex 4: 
import pandas as pd
import statsmodels.api as sm
import numpy as np

def autoregress_logit(df: pd.DataFrame) -> float:
    """
    The function performs data cleaning as #ex 3.
    The function transforms all values in delta_close into binary values using the sigmoid function.
    The function then runs a logistic regression of Delta_X on Delta_X_old without an intercept.
    The function then returns the t-value of the coefficient.
    """
    df['delta_close'] = df['Close'].diff()
    df['delta_close_old'] = df['delta_close'].shift(1)
    df = df.dropna()
    Delta_X = df['delta_close']
    Delta_X = 1 / (1 + np.exp(-Delta_X))
    Delta_X_old = df['delta_close_old']
    model4 = sm.Logit(Delta_X, Delta_X_old).fit()

    return model4.tvalues[0]
