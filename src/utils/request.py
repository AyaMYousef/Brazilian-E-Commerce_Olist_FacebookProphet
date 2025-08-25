from pydantic import BaseModel
from typing import List
import pandas as pd



# Request schema
class ForecastRequest(BaseModel):
    dates: List[str]   # list of future dates as strings (YYYY-MM-DD)



'''Example Request
{
  "dates": ["2025-01-15", "2025-02-20", "2025-03-10", "2025-04-05"]
}

'''