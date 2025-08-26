#Ex 0:
def github() -> str:    ####hgfghkjg
    """
    This code would give you a link to my GitHub Repository page!
    """

    return "https://github.com/zixuan28/ECON481_HWs/blob/main/481HW1.py"

#Ex 2:
def evens_and_odds(n: int) -> dict:
    """
    This code takes a for loop with two conditions: 
    the first condition take sum of values ranging from 1 to n-1 which are congruent to 0 modulo 2,
    and the second condition take sum of values ranging from 1 to n-1,
    which violates the first condition in modulo 2. 
    The first condition gives us the sum of evens below n and the second condition gives us the sum of odds below n.
    """
    evens = 0
    odds = 0
    for i in range(1, n):
        if i % 2 == 0:
            evens += i
        else:
            odds += i

    return {"evens": evens, "odds": odds}

#Ex 3:
from typing import Union

from datetime import datetime, date, time, timedelta

def time_diff(date_1: str, date_2: str, out: str) -> Union[str,float]:
    """
    This code first convert datetime strings into datetime objects,
    then the code take absolute values of the objects' difference and only display days.
    If the third argument in the function is float, only display the days of differnece.
    If the third argument in the function is string type, display a sentence with days of difference.
    """
    date_1 = datetime.strptime(date_1, "%Y-%m-%d")
    date_2 = datetime.strptime(date_2, "%Y-%m-%d")
    dt_diff = abs(date_1 - date_2).days
    if out == 'float':
        return dt_diff
        
    else:
        return f"There are {dt_diff} days between the two dates."

#Ex 4
def reverse(in_list: list) -> list:
    """
    This code would reverse the order of the list. 
    I make the first spot of the list the last element in original list,
    then I make the second spot the second to last element.
    The sequence go on until the end of the list.
    """
    new_list=[]
    for i in range(0, len(in_list)):
        x = in_list[-i-1]
        new_list.append(x)

    return new_list

#Ex 5
def prob_k_heads(n: int, k: int) -> float:
    """
    This code uses the binomial distribution formula, 
    where n is all flips and k is the number of heads among these flips.
    The binomial coefficient is calulated as the product of all integers from k+1 to n over (n-k)!
    Then, we just use the binomial distribution formula.
    """
    if n < k:
        return "Please enter valid values."
        
    else:
        n_minus_k_fac = 1
        for i in range(1, n-k+1):
            n_minus_k_fac *= i
            
        n_c_k = 1
        for i in range(k+1, n+1):
            n_c_k *= i
        
        n_c_k /= n_minus_k_fac
        
        prob = n_c_k * (0.5 ** k) * (0.5 ** (n-k))
        
        return prob
