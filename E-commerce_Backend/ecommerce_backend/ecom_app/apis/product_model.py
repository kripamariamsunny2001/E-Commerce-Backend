from pydantic import BaseModel

class Products(BaseModel):
    productName:str
    description:str
    amount:int
    rating:float
    productImage:str

class ResponseModel(BaseModel):
   productName:str
   description:str
   amount:int
   rating:float
   productImage:str
        