from pymongo import MongoClient

class MongoDB:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
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
