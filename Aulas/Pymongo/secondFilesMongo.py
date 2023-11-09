import collections
import datetime
from enum import unique
import pprint
from turtle import pos
import pymongo
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

# Contador de documentos a partir de um parametro 
print("\nTotal de documentos A partir de algum parametro especifico")
print("1:")
pprint.pprint(posts.count_documents({"author": "Gustavo"}))
print("\n2:")
pprint.pprint(posts.count_documents({"tags": "insert"}))

print("\n")
pprint.pprint(posts.find_one({"tags": "insert"}))


print("\nRecuperando info da coleção post de maneira ordenada:\n")
for post in posts.find({}).sort("date"):
    pprint.pprint(post)

result = db.profiles.create_index([('author', pymongo.ASCENDING)], unique=True)

# Lista Ordenada buscando os profiles e os index's
print("\n")
print(sorted(list(db.profiles.index_information())))
print("\n")

# Criando profiles de usuarios
user_profile_user = [
    {'user_id': 211, 'name': 'Luke'},
    {'user_id': 212, 'name': 'Claire'}]

# Inserindo dados para o Database
result = db.profile_user.insert_many(user_profile_user)

# Listar os nomes
print(db.list_collection_names())
print("\n")

# Listar as Coleções
print("Coleções armazenadas no MongoDB")
collections = db.list_collection_names()
for collections in collections:
    print(collections)

for post in posts.find():
    pprint.pprint(post)

# Deletar o documento a partir de um parametro
print(posts.delete_one({"author": "Joao"}))

# Drop apaga todos os documentos de uma collection
# print(db.profile_user.drop())

# Deletar o Banco de dados
# client.drop_database('test')


