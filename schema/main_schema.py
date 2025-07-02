from pydantic import BaseModel, Field
from typing import Annotated



class UserDetails(BaseModel):

    total_steps: Annotated[int, Field(..., title="Total Stpes", description="Total Steps coverd in a day (units)")]
    very_active_minutes: Annotated[int, Field(..., title="Very ACtive time", description="Your highly active time (in minutes)")]
    calories: Annotated[int, Field(..., title="Calories", description="Total Calories burned in a day (units)")]





