
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["college"]
sales = db["sales"]

print("Connected to MongoDB")

# 1. Insert sales records
sales.delete_many({})  # Clear old sample records

sales.insert_many([
    {"product": "Laptop", "month": "Jan", "sales": 50000},
    {"product": "Mobile", "month": "Jan", "sales": 30000},
    {"product": "Laptop", "month": "Feb", "sales": 60000},
    {"product": "Mobile", "month": "Feb", "sales": 40000},
    {"product": "Laptop", "month": "Mar", "sales": 70000}
])

# 2. Display all sales records
print("\nAll Sales Records:")
for record in sales.find({}, {"_id": 0}):
    print(record)

# 3. Calculate total sales by month
pipeline = [
    {"$sort": {"sales": -1}},
    {"$limit":1}
]

print("\nMonthly Sales Analysis:")
for result in sales.aggregate(pipeline):
    print(result)

# 6. Close connection
client.close()
print("\nConnection closed")
