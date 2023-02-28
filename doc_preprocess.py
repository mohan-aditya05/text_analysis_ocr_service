from db import MongoDB

class DocumentPreprocess:
    def __init__(self, file_bytes):
        self.file_bytes = file_bytes
        self.mongo = MongoDB()

    
    def process_document(self):
        pass