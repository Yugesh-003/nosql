
from pymongo import MongoClient

# 1. Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["college"]
sales = db["sales"]

print("Connected to MongoDB")

# 2. Insert sales records
records = [
    {"product": "Laptop", "month": "Jan", "sales": 50000},
    {"product": "Mobile", "month": "Jan", "sales": 30000},
    {"product": "Laptop", "month": "Feb", "sales": 60000},
    {"product": "Mobile", "month": "Feb", "sales": 40000},
    {"product": "Laptop", "month": "Mar", "sales": 70000}
]

# Run this insertion only once to avoid duplicate records
if sales.count_documents({}) == 0:
    sales.insert_many(records)

# 3. Retrieve and display records
print("\nAll Sales Records:")
for record in sales.find({}, {"_id": 0}):
    print(record)

# 4. Calculate total sales for each product
pipeline = [
    {
        "$group": {
            "_id": "$product",
            "totalSales": {"$sum": "$sales"}
        }
    },
    {"$sort": {"totalSales": -1}}
]

print("\nTotal Sales by Product:")
for result in sales.aggregate(pipeline):
    print(result)

# 5. Find the highest sales record
pipeline = [
    {"$sort": {"sales": -1}},
    {"$limit": 1},
    {"$project": {
        "_id": 0,
        "product": 1,
        "month": 1,
        "sales": 1
    }}
]

print("\nHighest Sales Record:")
for result in sales.aggregate(pipeline):
    print(result)

# 6. Close connection
client.close()
