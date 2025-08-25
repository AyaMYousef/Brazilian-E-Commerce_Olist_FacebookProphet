import pandas as pd
from typing import List
from .utils.request import ForecastRequest
from .utils.response import ForecastResponse
from src.utils.config import model




def make_forecast(dates: List[str]):
    new_data = pd.DataFrame({
        "ds": pd.to_datetime(dates)
    })
    forecast = model.predict(new_data)
    results = forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]]
    return results
