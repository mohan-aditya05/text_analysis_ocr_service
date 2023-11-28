from pymongo import MongoClient
from decouple import config

class MongoDB:
    def __init__(self):
        user_name = config("MONGODB_USER")
        password = config("MONGODB_PWD")
        cluster = config("MONGODB_CLUSTER")
        self.client = MongoClient(f'mongodb+srv://{user_name}:{password}@{cluster}/')
        self.db = self.client.text_analysis
        self.collection = self.db.ocr_response

    def insert_document(self, ipt):
        try:
            result = self.collection.insert_one(ipt)
        except:
            print("Error in inserting document")
            return False
        
        return True
    
    def query_document(self, key:dict):
        try:
            result = self.collection.find_one(key)
        except:
            print("Error in finding document")
            return False
        return result
