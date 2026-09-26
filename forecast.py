import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from prophet import Prophet

db_url = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="AshishThakur@18",
    host="localhost",
    database="supply_chain_db"
)
engine = create_engine(db_url)

print("Fetching historical data from MySQL...")
query = """
SELECT date AS ds, SUM(sales) AS y 
FROM cleaned_sales 
GROUP BY date 
ORDER BY date
"""
df = pd.read_sql(query, con=engine)

print("Training Prophet Model (this might take a few seconds)...")
model = Prophet()
model.fit(df)

print("Predicting next 30 days of demand...")
future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

final_forecast = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
final_forecast.rename(columns={'ds': 'date', 'yhat': 'predicted_sales', 'yhat_lower': 'min_sales', 'yhat_upper': 'max_sales'}, inplace=True)

print("Saving forecast results to MySQL...")
final_forecast.to_sql(name="forecast_results", con=engine, if_exists="replace", index=False)

print("Forecast complete and saved to Database successfully!")