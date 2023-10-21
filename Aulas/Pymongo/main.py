import datetime
import pprint
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://gustavo123:diodio@cluster1.lk7vsny.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
# try:
#    client.admin.command('ping')
#    print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#    print(e)

#Criando o Banco de dados
db = client.test
collection = db.test_collection

# Consultando dados da Database
print(db.list_collection_names())

# Path
# print(db.test_collection)

# Definição de Informação para compor o new Doc
post = {
    "author": "Gustavo",
    "text": "My First MongoDB application based on Python",
    "tags": ["mongodb", "python3", "pymongo"],
    "date": datetime.datetime.utcnow()
}

# Preparando para submeter as infos
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print("\n")
print(post_id)

print("\n")
print(db.posts)
print("\n")

# Recuperando o nome das Coleções
print(db.list_collection_names())

# Mostrando a função recuperada
# 1
print("\n")
print(db.posts.find_one())
print("\n")

# 2 (de forma Indentada)
pprint.pprint(db.posts.find_one())

