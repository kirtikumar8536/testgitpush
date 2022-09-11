import pymongo

client = pymongo.MongoClient("mongodb+srv://kkumar:mongodb123@cluster0.ctcpjzp.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)
d={
    "name":"sudhanshu",
    "email":"sudha@.ai",
    "surname":"kumar"
}

db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)