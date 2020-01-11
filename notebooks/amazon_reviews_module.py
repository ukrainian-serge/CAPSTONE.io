import pandas as pd
import numpy as np
import psycopg2
from sqlalchemy import create_engine

def pre_load(path, delim='\t', encoding='UTF-8') -> tuple:
    """
    Simple delimited text file reader.
    Returns  : tuple(header, body)

    path     : path to data
    delim    : file delimiter
    encoding : encoding
    """
    f=open(path, encoding=encoding)
    lines=f.readlines()
    header = lines[0].strip('\n').lower().split(delim)
    body = [row.strip('\n').split(delim) for row in lines[1:]]
    return header, body


def season_mapper(date=np.datetime64) -> str:
    """
    Season mapper
    Returns : str(season)

    date    : datetime
    """
    if date.month >= 3 and date.month < 6:
        return 'spring'
    elif date.month >= 6 and date.month < 9:
        return 'summer'
    elif date.month >= 9 and date.month < 12:
        return 'fall'
    return 'winter'


# stdout redirect to text
class RedirectStdStreams(object):
    def __init__(self, stdout=None, stderr=None):
        self._stdout = stdout or sys.stdout
        self._stderr = stderr or sys.stderr

    def __enter__(self):
        self.old_stdout, self.old_stderr = sys.stdout, sys.stderr
        self.old_stdout.flush(); self.old_stderr.flush()
        sys.stdout, sys.stderr = self._stdout, self._stderr

    def __exit__(self, exc_type, exc_value, traceback):
        self._stdout.flush(); self._stderr.flush()
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr
        
        
# FOR QUERY RUNS
def get_query_table(query="SELECT * FROM reviews limit 10",
                    engine=create_engine('postgresql+psycopg2://postgres:postgres@localhost/amazon_reviews'), 
                    parse_date='review_date', 
                    index_col='review_id') -> pd.DataFrame:
    """
    Simple DatFrame building function
    Returns : indexed, date-parsed DataFrame from database

    query       : query string
    engine      : psycopg2 engine
    parse_date  : column to parse date
    index_col   : column to use as index
    """
    return pd.read_sql(query, con=engine, parse_dates=parse_date, index_col=index_col)


# FOR AUTOMATE TABLE CREATE
def create_category_tables(list_of_categories=list, query_text=str, connection=psycopg2.connect) -> tuple:
    """
    PostgreSQL database connection and table creation function

                Returns:    Table list of tuples from information_schema.tables for verification of creation
                            Drops tables if they exist
                            Creates tables by 'product_category'
    
    list_of_categories :    'product_category' contained within `reviews` Table within `amazon_reviews` db
    query_text         :    text that is formatted using iterables within 'product_category' list
    connection         :    psycopg2.connection to database
    """
    cursor = connection.cursor()
    for i in list_of_categories:
        cursor.execute(query_text.format(i, i, i))
        connection.commit()
    cursor.execute("""
    SELECT 
        table_name 
    FROM information_schema.tables 
    WHERE table_schema='public'""")
    tables = cursor.fetchall()
    connection.close()
    return tables
        
        
        
        