from fastapi import APIRouter, Request, BackgroundTasks, HTTPException, Depends
from fastapi.responses import JSONResponse

from typing import Union
from controller import fitness as fn_agent

fitness_route = APIRouter()

@fitness_route.get('/workout-plan/{fitness_goal}')
async def get_workout_plan(r: Request, 
                           fitness_goal: str, 
                           instruction: Union[str, None]=None): 
    try: 
        response = await fn_agent.generate_workout_plan(fitness_goal, instruction)
        return JSONResponse(content=response,
                            status_code=200)
    except HTTPException as e: 
        return JSONResponse(content=e, 
                            status_code=404)