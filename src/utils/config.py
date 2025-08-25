import os
from dotenv import load_dotenv
import joblib

 
# load .env file
load_dotenv(override=True)


# get the variables
APP_NAME = os.getenv("APP_NAME")
VERSION= os.getenv("VERSION")
SECRET_KEY= os.getenv("SECRET_KEY")



SRC_FOLDER_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load  model
model = joblib.load(os.path.join(SRC_FOLDER_PATH, "artifacts", "prophet_model.pkl"))