import pymongo
from fastapi import FastAPI
# Connecting to DB 
mydb = pymongo.MongoClient('mongodb+srv://user:user@beachme.c5sbvhv.mongodb.net/?retryWrites=true&w=majority')["beachme-1"]
# Fetching "Shores"
shore_db = mydb.shores
# Creating api
app = FastAPI()

# Get all shores on db
@app.get("/get_all_shores")
async def root():
    shores = list(shore_db.find({}))
    for shore in shores:
        del shore['_id']
    return shores

# Get Specific shore by id
@app.get("/get_specific_shore/{id}")
async def root(id):
    # Converting from pymongo Cursor to list, then to object 
    shore = list(shore_db.find({"id":int(id)}))[0]
    del shore['_id']
    return shore
