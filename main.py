from model import Company
from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

from database import(
    fetch_all_companys,fetch_one_company,remove_Compnay,update_company,create_company
)

origins=['https://localhost:300']


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/comapny/{name}",response_model=Company)
async def get_company(name):
    response =await fetch_one_company(name)
    if response:
        return response
    raise HTTPException(404,f"there is no company with the name {name}")

@app.post("/add",response_model=Company)
async def add_company(company:Company):
    response=await create_company(company.dict())
    if response:
        return response
    raise HTTPException(400, "something went wrong")
    

@app.delete("/delete/{name}")
async def del_company(name):
    reponse=await remove_Compnay(name)
    if reponse:
        return f"sucessfully deleted the company"

    raise HTTPException(404,f"there is no company with the name{name}")

@app.put("/update/{emp_size}",response_model=Company)
async def update_details(name:str,emp_size:int):
    response =await update_company(name,emp_size)
    if response:
        return response
    raise HTTPException(404,f"there is no company with the name{name}")

@app.get("/all")
async def show_all_comapanys():
    response =await fetch_all_companys()
    return response