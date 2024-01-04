# Copyright 2023 Aditya Mohan

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from decouple import config
from pymongo import MongoClient

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
