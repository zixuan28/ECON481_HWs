import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

path = 'auctions.db' #This is the file path to the database auctions.db, I used JupterHub
engine = create_engine(f'sqlite:///{path}')

class DataBase:
    def __init__(self, loc: str, db_type: str = "sqlite") -> None:
        """Initialize the class and connect to the database"""
        self.loc = loc
        self.db_type = db_type
        self.engine = create_engine(f'{self.db_type}:///{self.loc}')
    def query(self, q: str) -> pd.DataFrame:
        """Run a query against the database and return a DataFrame"""
        with Session(self.engine) as session:
            df = pd.read_sql(q, session.bind)
        return(df)

auctions = DataBase(path)

#Ex 0:
def github() -> str:
    """
   This code would give you a link to my GitHub Repository page!
    """

    return "https://github.com/zixuan28/ECON481_HWs/blob/main/481HW6.py"

#Ex 1:
def std() -> str:
    """
    The first part of the function is the CTE that calculates the average bid for each item.
    The second part of the function calculates the standard deviation of the bid amounts for each item.
    Then, the function joins the two parts and calculates the standard deviation for each item.
    Lastly, the function returns the item ID and the standard deviation of the bid amounts for each item.
    """
    q = """
    WITH AvgBids AS (
        SELECT itemId, AVG(bidAmount) AS avg_bid
        FROM bids
        GROUP BY itemId
        HAVING COUNT(bidAmount) > 1
    )
    SELECT a.itemId 
           ,(CASE WHEN COUNT(b.bidAmount) > 1 THEN 
                ROUND(SQRT(SUM((b.bidAmount - a.avg_bid) * (b.bidAmount - a.avg_bid)) / (COUNT(b.bidAmount) - 1)), 4) 
            ELSE 
                NULL 
            END) as std
    FROM bids b
    JOIN AvgBids a ON b.itemId = a.itemId
    GROUP BY b.itemId
    HAVING COUNT(b.bidAmount) > 1;
    """
    
    return print(auctions.query(q))
