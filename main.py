from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware
from src.utils.request import ForecastRequest
from src.utils.response import ForecastResponse
from src.inference import make_forecast
from typing import List
from dotenv import load_dotenv
import os
load_dotenv()



app = FastAPI(title=os.getenv('APP_NAME'), version=os.getenv('VERSION'))
app.add_middleware(
   CORSMiddleware,
   allow_origins=["*"],
   allow_methods=["*"],
   allow_headers=["*"],
)


api_key_header = APIKeyHeader(name='X-API-Key')
async def verify_api_key(api_key: str=Depends(api_key_header)):
    if api_key != os.getenv('SECRET_KEY'):
        raise HTTPException(status_code=403, detail="You are not authorized to use this API")
    return api_key

@app.get('/', tags=['check'])
async def home(api_key: str=Depends(verify_api_key)):
    return {
        "message": "up & running"
    }



@app.post("/forecast", response_model=List[ForecastResponse])
async def forecast(request: ForecastRequest, api_key: str = Depends(verify_api_key)):
    try:
        forecast_df = make_forecast(request.dates)
        response = [
            ForecastResponse(
                ds=str(row["ds"].date()),
                yhat=row["yhat"],
                yhat_lower=row["yhat_lower"],
                yhat_upper=row["yhat_upper"]
            )
            for _, row in forecast_df.iterrows()
        ]
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error making predictions: {str(e)}")
