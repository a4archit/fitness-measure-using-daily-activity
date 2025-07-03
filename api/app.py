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


'''
heart_rate: float,
blood_oxygen_level: float,
steps_counts: int,
sleep_duration: float,
activity_level: Literal[0,1,2]
'''

## prediction route
@app.post("/predict")
def predict(details: UserDetails):

    # fetching user details
    heart_rate = details.heart_rate
    blood_oxygen_level = details.blood_oxygen
    steps_counts = details.steps
    sleep_durations = details.sleep_duration
    activity_level = details.activity_level

    prediction = model.predict(
        heart_rate=heart_rate,
        blood_oxygen_level=blood_oxygen_level,
        steps_counts=steps_counts,
        sleep_duration=sleep_durations,
        activity_level=activity_level
    )

    prediction_msg = "Person is physically fit." if prediction else "Person is not physically fit."

    content: dict = {
        'prediction value': prediction,
        'prediction message': prediction_msg,
        'input details': {
            'msg':'updates will soon............'
        }
    }

    return JSONResponse(status_code=200, content=content)



