import math

import pandas as pd
from bson import ObjectId
from fastapi import FastAPI, HTTPException

from PandatoMongo import get_collection

app = FastAPI()
collection = get_collection("filtered_orders")

@app.get("/records")
def get_records():
    try:
        records = list(collection.find().limit(50))
        print("in get records function")
        for record in records:
            record["_id"] = str(record["_id"])  # Convert ObjectId to string
        return records
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/records/")
def add_records(data:dict):
    new_record = collection.insert_one(data)
    return {"inserted_id":str(new_record.inserted_id)}

@app.delete("/records/{record_id}")
def remove_record(record_id:str):
    delete_record = collection.delete_one({"_id":ObjectId(record_id)})
    if delete_record.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Record not found")
    return {"message": "Record deleted successfully"}
