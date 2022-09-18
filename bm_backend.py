import pymongo
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Connecting to DB
mydb = pymongo.MongoClient(
    'mongodb+srv://user:user@beachme.c5sbvhv.mongodb.net/?retryWrites=true&w=majority')["beachme-1"]
# Fetching "Shores"
shore_db = mydb.shores
# Creating api
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Get all shores on db


@app.get("/get_all_shores")
async def root():
    shores = list(shore_db.aggregate([{"$sample": {"size": 4}}]))
    for shore in shores:
        del shore['_id']
    return shores

# Get Specific shore by id


@app.get("/get_specific_shore/{id}")
async def root(id):
    # Converting from pymongo Cursor to list, then to object
    shore = list(shore_db.find({"shore_id": int(id)}))[0]
    del shore['_id']
    return shore
