# pip install pymongo

from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["company"]
sales = db["sales"]

print("Connected to MongoDB")

# 4. Close connection
client.close()
print("\nConnection closed")
