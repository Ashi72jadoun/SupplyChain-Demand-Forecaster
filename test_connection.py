from sqlalchemy import create_engine
from sqlalchemy.engine import URL

db_url = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="AshishThakur@18",
    host="localhost",
    database="supply_chain_db"
)

engine = create_engine(db_url)

try:
    connection = engine.connect()
    print("Database Connection Successful!")
    connection.close()
except Exception as e:
    print(f"Connection Failed: {e}")