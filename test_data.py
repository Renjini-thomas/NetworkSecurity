from pymongo import MongoClient
from urllib.parse import quote_plus

  # encodes special characters

uri = f"mongodb+srv://renjini2539thomas:<@password>@cluster0.4g0vvli.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
