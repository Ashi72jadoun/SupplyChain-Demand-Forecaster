import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

print("Reading Kaggle data...")
df = pd.read_csv("train.csv")

print("Filtering data for Store 1...")
df = df[df['store_nbr'] == 1]

print("Cleaning data...")
df['sales'] = df['sales'].fillna(0.0)
df['date'] = pd.to_datetime(df['date'])

db_url = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="AshishThakur@18",
    host="localhost",
    database="supply_chain_db"
)
engine = create_engine(db_url)

print("Loading data into MySQL...")
df.to_sql(name="cleaned_sales", con=engine, if_exists="replace", index=False)

print("Real Data loaded to MySQL successfully!")