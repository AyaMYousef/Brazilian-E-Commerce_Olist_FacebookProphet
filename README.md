# Evaluating Delivery Performance and Operational Efficiency

This repository focuses on analyzing and forecasting delivery performance using the **Brazilian E-Commerce Public Dataset by Olist**, coupled with a real-time **FastAPI inference service** for delivery forecasting.

---

## Dataset

We use the **Brazilian E-Commerce Public Dataset by Olist** from Kaggle. It includes roughly **100,000 orders** from 2016 to 2018, covering multiple key aspects:

* Order information: timestamps (purchase, approval, carrier delivery, customer delivery), estimated delivery date, order status, etc.
* Product details: pricing, freight, category, and seller IDs.
* Customer data: location (city/state, zip code).
* Seller data: location and identification.
* Payment methods, installments, and values.
* Including review data from customers.

This rich dataset enables comprehensive analysis—from delivery reliability to geographic and seasonal trends.([Kaggle][1], [Medium][2])

---

## Motivation & Business Context

Delivery process efficiency is a critical driver of customer satisfaction and retention:

* A McKinsey study (2016) found **25% of consumers abandon a retailer after just one late delivery**.
* Bain & Company (Reichheld 2001) shows businesses with reliable logistics reduce churn and improve loyalty.

Thus, delivery analytics becomes a key strategic lever—focusing on service reliability to maximize value rather than only cutting costs.

---

## Objectives

This work aims to analyze and forecast delivery performance—providing insights to enhance logistics, customer experience, and operational performance. Managers should be able to:

* Determine how often deliveries are **early, on time, or late**.
* Measure the **average delay** and pinpoint product categories with the most delays.
* Analyze **fulfillment timelines**, such as Purchase → Approval → Shipment → Delivery, and identify bottlenecks.
* Understand the effects of **seasonality, holidays, and high-demand periods** on delays.
* Compare **delivery reliability across states, regions, and sellers**, and spot best/worst-performing routes.
* Track key KPIs: average delivery time by region, percentage of on-time deliveries, seller-based reliability.

---

## Tech Stack

* **Python 3.10**
* **Facebook Prophet** – time series forecasting
* **Pandas, NumPy** – data handling and manipulation
* **FastAPI** – serving the forecasting model as an API
* **Uvicorn** – ASGI server for running the FastAPI app

---

## FastAPI Inference Service

The Prophet model loads via joblib and exposes a `/forecast` endpoint to process date lists and return delivery forecasts.

**Example Request** to `POST /forecast`:

```json
{
  "dates": ["2025-01-15", "2025-02-20", "2025-03-10"]
}
```

**Example Response**:

```json
[
  {"ds": "2025-01-15", "yhat": 123.4, "yhat_lower": 110.2, "yhat_upper": 140.6},
  {"ds": "2025-02-20", "yhat": 135.7, "yhat_lower": 120.5, "yhat_upper": 150.8},
  {"ds": "2025-03-10", "yhat": 145.2, "yhat_lower": 130.1, "yhat_upper": 160.3}
]
```

Use the interactive Swagger UI available at `http://127.0.0.1:8000/docs` once the server is running.

---

## Installation & Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/AyaMYousef/Brazilian-E-Commerce_Olist_FacebookProphet.git
   cd Brazilian-E-Commerce_Olist_FacebookProphet
   ```

2. Set up a Python virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the FastAPI application:

   ```bash
   uvicorn src.main:app --reload
   ```

---

## Project Structure

```
Brazilian-E-Commerce_Olist_FacebookProphet/
│
├── src/                     # Source code
│   ├── main.py              # FastAPI entrypoint
│   ├── utils/               # Config, data loading, helper functions
│   └── artifacts/           # Trained Prophet model (pickle file)
│
├── notebooks/               # Jupyter notebooks (EDA, model building, evaluation)
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── .gitignore               # Files and directories to ignore
```

---

## Insights (Highlights)

* **Geographic disparity** in delivery performance revealed regional bottlenecks.
* During **high-demand or sales periods**, delivery delays increased notably.
* The **Approval → Shipment** stage surfaced as a common bottleneck.
* Some seller–customer routes disproportionately impact on-time delivery metrics.

---

## Future Directions

* Add **API authentication** (e.g. API key via `Depends(verify_api_key)`).
* Deploy the app with **Docker** and orchestrate with Kubernetes or cloud services.
* Integrate with dashboards (like Power BI or Tableau) for real-time business reporting.

---

## References

* McKinsey & Company (2016). *The Future of Last-Mile Logistics*
* Reichheld, F. (2001). *The Loyalty Effect*. Bain & Company.
* Brazilian E-Commerce Public Dataset by Olist (Kaggle) ([Kaggle][1], [Medium][2])

---

✨ **Author**: [AyaMYousef](https://github.com/AyaMYousef)

