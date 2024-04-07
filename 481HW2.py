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

#Ex 2:
import numpy as np
import scipy as sp

def estimate_mle(y: np.array, X: np.array) -> np.array:
    """
    This code returns to the estimated coefficients of a sample regression.
    The MLE is the negative log likelihood function for normal distribution.
    The minimization function takes the MLE and return the estimated coefficients.
    """
    x_0 = np.zeros(X.shape[1]+1)
    X_int = np.c_[np.ones(X.shape[0]).reshape(-1,1), X]
    
    def MLE(beta: np.array, y: np.array, X: np.array) -> np.array:
        y_hat = np.dot(X_int, beta)
        e_hat = y - y_hat
        log_normal = np.log(1 / np.sqrt(2 * np.pi)) - 0.5 * np.square(e_hat)
        
        return -np.sum(log_normal)

    result = sp.optimize.minimize(
        fun = MLE, 
        x0 = x_0, 
        args = (y.reshape(1, -1), X_int),
        method='Nelder-Mead'
    )
    
    return result.x.reshape(-1,1)

#Ex 3:
import numpy as np
import scipy as sp

def estimate_ols(y: np.array, X: np.array) -> np.array:
    """
    This code returns to the estiamted coefficients of a sample regression.
    The OLS is the sum of residual squares.
    The minimization functions performs the OLS method and returns beta hats.
    """
    x_0 = np.zeros(X.shape[1]+1)
    X_int = np.c_[np.ones(X.shape[0]).reshape(-1,1), X]

    def OLS(beta: np.array, y: np.array, X: np.array) -> np.array:
        y_hat = np.dot(X_int, beta)
        e_hat = y - y_hat
        ols_func = np.sum(np.square(e_hat))
        
        return ols_func

    result = sp.optimize.minimize(
        fun = OLS, 
        x0 = x_0, 
        args = (y.reshape(1, -1), X_int),
        method='Nelder-Mead'
    )

    return result.x.reshape(-1,1)