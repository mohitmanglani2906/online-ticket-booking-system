import pymongo
import os
from dotenv import load_dotenv
load_dotenv()

def connectWithMongo(dbName: str):
    connection_string = os.getenv('MONGO_DB_CONNECTION_STRING')
    client = pymongo.MongoClient(connection_string)
    db = client[dbName]
    return db

def saveData(record: dict, dbName: str, tableName: str):
    db = connectWithMongo(dbName)
    rec = db[tableName].insert_one(record)
    # print(rec.acknowledged)

def createIndex(dbName: str, fieldName: str, tableName: str):
    db = connectWithMongo(dbName)
    test = db[tableName].create_index([(fieldName, pymongo.TEXT)])
    # print(test)

def searchPNR(dbName: str, tableName: str, pnrRecord: str):
    db = connectWithMongo(dbName)
    try:
        ticketRecord = dict()
        cursor = db[tableName].find({'$text': {
                '$search': pnrRecord
            }}
        )
        for c in cursor:
            ticketRecord.update(c)
        return ticketRecord
    except Exception as e:
        print(e.args)
        return {}