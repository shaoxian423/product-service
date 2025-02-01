from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Load environment variables
PORT = int(os.getenv("PORT", 3030))  # 从环境变量获取 PORT，默认为 3030

# Define a CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE"],  # Allows GET, POST, DELETE methods
    allow_headers=["*"],  # Allows all headers
)

# Define a product model using Pydantic for data validation
class Product(BaseModel):
    id: int
    name: str
    price: float

# In-memory store for products
products = [
    {"id": 1, "name": "Dog Food", "price": 19.99},
    {"id": 2, "name": "Cat Food", "price": 34.99},
    {"id": 3, "name": "Bird Seeds", "price": 10.99},
]

# Define the GET endpoint for products
@app.get("/products", response_model=List[Product])
async def get_products():
    return products

# Define the POST endpoint to add a product
@app.post("/add-product", response_model=Product)
async def add_product(product: Product):
    products.append(product.dict())  # Add the new product to the store
    return product

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3030)
