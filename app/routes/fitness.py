from fastapi import APIRouter, Request, HTTPException, Depends
from fastapi.responses import JSONResponse

from controller.workout_plan import generate_workout_plan
from b2m.schema import GetWorkoutPlan

fitness_route = APIRouter()

@fitness_route.post('/workout-plan')
async def get_workout_plan(fitness_goal: GetWorkoutPlan): 
    try: 
        response = await generate_workout_plan(fitness_goal)
        return JSONResponse(content=response,
                            status_code=200)
    except HTTPException as e: 
        return JSONResponse(content=e, 
                            status_code=404)