from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel, Field
from math_functions import add, subtract, multiply, divide
import logging
import uvicorn

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

class OperationInput(BaseModel):
    a: float = Field(..., description="First number")
    b: float = Field(..., description="Second number")
    operation: str = Field("add", description="Operation to perform: add, subtract, multiply, divide")

@app.get("/")
async def root(input: OperationInput = Query(...)):
    logger.info(f"Received request with input: {input}")
    if input.operation == "add":
        result = add(input.a, input.b)
    elif input.operation == "subtract":
        result = subtract(input.a, input.b)
    elif input.operation == "multiply":
        result = multiply(input.a, input.b)
    elif input.operation == "divide":
        result = divide(input.a, input.b)
    else:
        logger.error(f"Invalid operation: {input.operation}")
        raise HTTPException(status_code=400, detail="Invalid operation")
    
    if isinstance(result, str) and result.startswith("Error"):
        logger.error(f"Operation error: {result}")
        raise HTTPException(status_code=400, detail=result)
    
    return {"message": "Hello World", "value": result}

@app.get("/health")
async def health():
    return {"status": "API is healthy"}