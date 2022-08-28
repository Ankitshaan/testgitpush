import pymongo

client = pymongo.MongoClient("mongodb+srv://Shaanankit119:Shaan123@cluster0.1metprh.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name": "ankit",
    "email": "abc@gmail.com",
    "surname": "kumar"

}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
