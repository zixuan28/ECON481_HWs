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

#Ex 2:
def bidder_spend_frac() -> str:
    """
    First, the function find the winning bidder by selecting the longest bidtime for each item.
    The function then calculates the total number of bids for each bidder.
    Then, the function calculates the total spend for each bidder.
    Lastly, the function joins the two parts and calculates the spend fraction for each bidder.
    """
    q2 = """
    WITH Sumbidder AS (
        SELECT HighbidderName AS bidderName, SUM(bidAmount) AS total_spend
        FROM (
            SELECT b1.HighbidderName, b1.bidAmount
            FROM bids b1
            JOIN (
                SELECT itemId, MAX(bidTime) AS latest_timestamp
                FROM bids
                GROUP BY itemId
            ) b2 ON b1.itemId = b2.itemId AND b1.bidTime = b2.latest_timestamp
        ) latest_bids
        GROUP BY bidderName
    ), 
    TotalBids AS (
        SELECT bidderName, MAX(bidAmount) AS total_bids
        FROM bids
        GROUP BY bidderName
    )
    SELECT s.bidderName, s.total_spend, t.total_bids, (s.total_spend / t.total_bids) AS spend_frac
    FROM Sumbidder s
    JOIN TotalBids t ON s.bidderName = t.bidderName;
    """
    return print(auctions.query(q2))

#Ex 3:
def min_increment_freq() -> str:
    """
    The function first find the frequency with which a bid is placed at the minimum increment for each item.
    Then, the function check if the new bid amount is bigger than the previous bid amount.
    If the new bid amount is bigger than the previous bid amount, the function calculates the frequency.
    """
    q3 = """
    SELECT 
        SUM(CASE 
                WHEN b2.bidAmount = b1.bidAmount + i.bidIncrement THEN 1
                ELSE 0
            END) * 1.0 / COUNT(b2.bidAmount) AS freq
    FROM bids b1
    JOIN bids b2 ON b1.itemId = b2.itemId AND b1.bidAmount < b2.bidAmount
    JOIN items i ON i.itemId = b1.itemId
    WHERE i.isBuyNowUsed = 0
    GROUP BY b1.itemId;
    """
    return print(auctions.query(q3))

#Ex 4:

def win_perc_by_timestamp() -> str:
    """
    The function first calculates the start and end time for each auction.
    Then, the function calculates the normalized time for each bid.
    The function then finds the winning bid for each item.
    Lastly, the function calculates the win percentage for each timestamp bin.
    """
    q4 = """
    WITH AuctionTimes AS (
        SELECT
            itemId, MIN(bidTime) AS startTime, MAX(bidTime) AS endTime
        FROM bids
        GROUP BY itemId
    ),
    BidsWithNormalizedTime AS (
        SELECT
            b.itemId, b.bidTime, b.bidAmount, t.startTime, t.endTime,
            CASE
                WHEN (julianday(t.endTime) - julianday(b.bidTime)) / (julianday(t.endTime) - julianday(t.startTime)) < 0.1 THEN 1
                WHEN (julianday(t.endTime) - julianday(b.bidTime)) / (julianday(t.endTime) - julianday(t.startTime)) < 0.2 THEN 2
                WHEN (julianday(t.endTime) - julianday(b.bidTime)) / (julianday(t.endTime) - julianday(t.startTime)) < 0.3 THEN 3
                WHEN (julianday(t.endTime) - julianday(b.bidTime)) / (julianday(t.endTime) - julianday(t.startTime)) < 0.4 THEN 4
                WHEN (julianday(t.endTime) - julianday(b.bidTime)) / (julianday(t.endTime) - julianday(t.startTime)) < 0.5 THEN 5
                WHEN (julianday(t.endTime) - julianday(b.bidTime)) / (julianday(t.endTime) - julianday(t.startTime)) < 0.6 THEN 6
                WHEN (julianday(t.endTime) - julianday(b.bidTime)) / (julianday(t.endTime) - julianday(t.startTime)) < 0.7 THEN 7
                WHEN (julianday(t.endTime) - julianday(b.bidTime)) / (julianday(t.endTime) - julianday(t.startTime)) < 0.8 THEN 8
                WHEN (julianday(t.endTime) - julianday(b.bidTime)) / (julianday(t.endTime) - julianday(t.startTime)) < 0.9 THEN 9
                ELSE 10
            END AS timestamp_bin
        FROM bids b
        JOIN AuctionTimes t ON b.itemId = t.itemId
    ),
    WinningBids AS (
        SELECT itemId, MAX(bidAmount) AS highestBidAmount
        FROM bids
        GROUP BY itemId
    )
    SELECT
        n.timestamp_bin,
        100.0 * SUM(CASE WHEN n.bidAmount = w.highestBidAmount THEN 1 ELSE 0 END) / COUNT(*) AS win_perc
    FROM BidsWithNormalizedTime n
    JOIN WinningBids w ON n.itemId = w.itemId
    GROUP BY n.timestamp_bin
    """
    return print(auctions.query(q4))