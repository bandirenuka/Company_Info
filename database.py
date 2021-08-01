from model import Company
import motor.motor_asyncio
from typing import List

client=motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
database=client.Companyd
collection=database.Companyt



async def create_company(company):
    document=company
    result=await collection.insert_one(document)
    return document


async def fetch_one_company(name):
    document = await collection.find_one({"name":name})
    return document

async def fetch_all_companys():
    companys=[]
    cursor=collection.find({})
    async for document in cursor:
        companys.append(Company(**document))
    return companys

async def update_company(name,employee_size):
    await collection.update_one({"name":name},{"$set":{"employee_size":employee_size}})
    document=await collection.find_one({"name":name})
    return document


async def remove_Compnay(name):
    await collection.delete_one({"name":name})
    return True