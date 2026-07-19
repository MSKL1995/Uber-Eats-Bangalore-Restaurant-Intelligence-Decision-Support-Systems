import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

BASE_DIR = Path(__file__).resolve().parent.parent

restaurants = pd.read_csv(
    BASE_DIR / "data" / "Uber_Eats_data.csv",
    encoding="utf-8"
)
orders = pd.read_json(BASE_DIR / "data" / "orders.json")

restaurants.rename(columns={
    "approx_cost(for two people)": "approx_cost_for_two",
    "listed_in(type)": "listed_in_type",
    "listed_in(city)": "listed_in_city"
}, inplace=True)

engine = create_engine(
    "mysql+pymysql://root:root@localhost:3306/uber_eats"
)

restaurants.to_sql(
    "restaurants",
    con=engine,
    if_exists="append",
    index=False
)

print("Restaurant data imported successfully!")

orders.to_sql(
    "orders",
    con=engine,
    if_exists="append",
    index=False
)

print("Order data imported successfully!")