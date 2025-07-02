# Dependencies
from fastapi import FastAPI, Path, Query, HTTPException
from fastapi.responses import JSONResponse

from typing import List, Dict, Optional, Annotated
from scripts.model_scripts import FitnessMeasure
from schema.main_schema import UserDetails


## setup model
model = FitnessMeasure()


## create an instance of FastAPI class
app = FastAPI()




## creating routes ------------------------------------------------------------------------------------------------------

# general route (/)
@app.get("/")
def general_routes():
    """ this function will display the basic information of the routes """

    routes_basic_info: dict = {
        "message": "welcome in fitness measure model's api",
        "routes": {
            "/predict": "this will used to predict 'Is  person physically fit or not?'"
        }
    }

    return JSONResponse(status_code=200, content=routes_basic_info)




## prediction route
@app.post("/predict")
def predict(details: UserDetails):

    # fetching user details
    steps = details.total_steps
    active_time = details.very_active_minutes
    calories = details.calories

    prediction = model.predict(
        total_steps=steps,
        very_active_minutes=active_time,
        calories=calories
    )

    prediction_msg = "Person is physically fit." if prediction else "Person is not physically fit."

    content: dict = {
        'prediction value': prediction,
        'prediction message': prediction_msg,
        'input details': {
            'total steps': steps,
            'very active time': active_time,
            'calories': calories
        }
    }

    return JSONResponse(status_code=200, content=content)



