# text_analysis_ocr_service

This repository contains the code for the OCR API service using the Flask backend. This is used
in conjunction with the Streamlit Information Extraction application
[https://github.com/mohanbing/st_doc_ext].

## Create and activate a venv
```bash
python -m venv <name_of_the_env>
source <name_of_the_env>/bin/activate
```


## Pip install all requirements

```bash
pip install -r requirements.txt
```

## Create .env file to specify the MongoDB credentials

```
MONGODB_USER = <user_name> 
MONGODB_PWD = <password>
MONGODB_CLUSTER = <cluster name>
```

Do check out the db.py file to check out the implementation of MongoDB caching and the
required database name and collection name.
