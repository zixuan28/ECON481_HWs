#Ex 0:
def github() -> str:
    """
    This code would give you a link to my GitHub Repository page!
    """

    return "https://github.com/zixuan28/ECON481_HWs/blob/main/481HW2.py"

#Ex 1:
import numpy as np

def simulate_data(seed: int = 481 ) -> tuple:
    """
    This code uses the random number generater with seed = 481.
    First, I draw 3000 numbers from normal distribution with mean 0 and variance 2.
    Then, I reshape the samples to a 1000 by 3 matrix.
    Second, I draw 1000 numbers from the standard normal distribution.
    Third, I made a 1000 by 1 matrix with only 5s.
    Last, I add up all the variables with the provided formula.
    """
    rng = np.random.default_rng(481)
    X = rng.normal(0, np.sqrt(2), 3000).reshape(-1, 3)
    Epsi = rng.standard_normal(1000).reshape(-1,1)
    Five = (np.ones(1000) * 5).reshape(-1,1)
    y = Five + 3*X[:,0:1] + 2*X[:,1:2] + 6*X[:,2:3] + Epsi

    return (y, X)