import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

print(myclient.list_database_names())

dblist = myclient.list_database_names()

if "mydatabase" in dblist:
  
  print("The database exists.")


myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

mycol = mydb["customers"]

collist = mydb.list_collection_names()

if "customers" in collist:
  
  print("The collection exists.")
