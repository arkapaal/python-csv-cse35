import pandas as pd
import numpy as np
from datetime import datetime, timedelta


np.random.seed(123)

num_records = 10

start_date = datetime.now() - timedelta(days=365)
random_dates = [start_date + timedelta(days=np.random.randint(0, 365)) for _ in range(num_records)]

data = {
    "ProductID": [f"PRD{str(i).zfill(4)}" for i in range(1, num_records + 1)],
    "Category": np.random.choice(["Electronics", "Clothing", "Food", "Books", "Toys"], num_records),
    "Price": np.random.uniform(5.99, 999.99, num_records).round(2),
    "Stock": np.random.randint(0, 500, num_records),
    "Discount": np.random.choice([0, 5, 10, 15, 20, 25], num_records),
    "LastRestocked": [date.strftime("%Y-%m-%d") for date in random_dates]
}

df = pd.DataFrame(data)

df.to_csv("product_inventory.csv", index=False)

print("CSV file created successfully!")
print("\nDataFrame Preview:")
print(df)
print(f"\nShape: {df.shape[0]} rows, {df.shape[1]} columns")
print(f"\nColumn Types:\n{df.dtypes}")