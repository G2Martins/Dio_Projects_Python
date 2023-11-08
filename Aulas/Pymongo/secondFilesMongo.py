import datetime
import pprint
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://gustavo123:diodio@cluster1.lk7vsny.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))

db = client.test
posts = db.posts

for post in posts.find():
    pprint.pprint(post)

# Contador dos documentos presentes
print("\nTotal de documentos")
print(posts.count_documents({}))

print("\nTotal de documentos A partir de algum parametro especifico")
print("1:")
pprint.pprint(posts.count_documents({"author": "Gustavo"}))
print("\n2:")
pprint.pprint(posts.count_documents({"tags": "insert"}))

print("\n")
pprint.pprint(posts.find_one({"tags": "insert"}))