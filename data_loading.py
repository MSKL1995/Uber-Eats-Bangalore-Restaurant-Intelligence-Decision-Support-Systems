from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

restaurants = pd.read_csv(BASE_DIR / "data" / "Uber_Eats_data.csv")
orders = pd.read_json(BASE_DIR / "data" / "orders.json")

print("="*50)
print("Restaurant Dataset")
print("="*50)

print(restaurants.info())

print()

print(restaurants.describe(include="all"))

print()

print(restaurants.isnull().sum())

print()

print("Duplicate Rows :", restaurants.duplicated().sum())

print("\n")

print("="*50)
print("Orders Dataset")
print("="*50)

print(orders.info())

print()

print(orders.describe(include="all"))

print()

print(orders.isnull().sum())

print()

print("Duplicate Rows :", orders.duplicated().sum())