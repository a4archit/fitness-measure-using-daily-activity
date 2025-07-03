from pydantic import BaseModel, Field
from typing import Annotated, Literal






class UserDetails(BaseModel):

    heart_rate: Annotated[float, Field(..., title="Heart Rate", description="Heart rate (BPM)")]
    blood_oxygen: Annotated[float, Field(..., title="Blood Oxygen level", description="Blood oxygen level (floating value)")]
    steps: Annotated[int, Field(..., title="Total Stpes", description="Total Steps coverd in a day (units)")]
    sleep_duration: Annotated[float, Field(..., title="Sleep duration", description="Sleep duration (in hrs)")]
    activity_level: Annotated[Literal[0,1,2], Field(..., title="Activity Level", description="Activity levels as: 0 for bad, 1 for good, and 2 for very good activity")]





