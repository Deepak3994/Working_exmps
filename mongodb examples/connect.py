from pymongo import MongoClient
import pymongo

client = MongoClient()
#which database to connect
db = client.file
contents = db.collection_name.find({})
#to aggregate based on the condition
#contents1 = db.courses.aggregate(
#	                        [
#	                         {"$match": {"name": "Mongodb"}},
#	                         {"$group":{"_id":"name","count":{"$sum":1}}}
#	                        ]
#	                       )
#contents2 = db.courses.create_index([("name", pymongo.ASCENDING)])
#printing the contents of the database
for document in contents:
	print(document)
