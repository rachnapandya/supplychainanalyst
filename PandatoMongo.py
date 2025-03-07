# %%
import numpy as np
import pandas as pd

# %%
df = pd.read_csv('Customer_support_data.csv')
columns_to_keep = [
    "Unique id",
    "channel_name",
    "category",
    "Customer Remarks",
    "Order_id",
    "order_date_time",
    "Issue_reported at",
    "issue_responded",
    "Customer_City",
    "Item_price"
]
df = df[columns_to_keep]
# %%
df_trimmed = df.head(1000)

# %%
##print(df_trimmed)

# %%
df.replace([np.nan, np.inf, -np.inf], None, inplace=True)
##print("hi")
# %%
import pandas as pd
from pymongo import MongoClient

# %%
data_dict = df.to_dict(orient="records")
# %%
client = MongoClient("mongodb://localhost:27017/")
db = client["customer_data"]
collection = db["filtered_orders"]
collection.insert_many(data_dict)

#%%
##print("data updated:)")

# %%
first_record = collection.find_one()

# %%
print(first_record)

# %%

def get_collection(collection_name):
    return db[collection_name]


# %%
