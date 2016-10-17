import sys
import pandas as pd 
import pymongo
import json
import os


def import_content(filepath):

	mng_client = pymongo.MongoClient()
	mng_db = mng_client.file
	#creating the collection name
	collection_name = 'data_base'
	db = mng_db.collection_name
	cdir = os.path.dirname(__file__)
	file_res = os.path.join(cdir, filepath)
    data = pd.read_csv(file_res)
	data_json = json.loads(data.to_json(orient='records'))
	db.remove()
	db.insert(data_json)

#main function
if __name__ == '__main__':
	filepath = '/home/deepak/Documents/Sois/Statistics/data.csv'
import_content(filepath)
