from pydantic import BaseModel
from typing import  List


# Response schema
class ForecastResponse(BaseModel):
    ds: str
    yhat: float
    yhat_lower: float
    yhat_upper: float




'''[
  {
    "ds": "2025-01-15",
    "yhat": 123.45,
    "yhat_lower": 100.12,
    "yhat_upper": 150.78
  },
  {
    "ds": "2025-02-20",
    "yhat": 140.67,
    "yhat_lower": 120.50,
    "yhat_upper": 160.34
  }
]
   ''' 