__author__="Minh Le"
__version__="0.0.0"

import logging
import uvicorn

from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware

from routes.fitness import fitness_route

route_list = [fitness_route]

origins = [
    "http://localhost:8000",    # From back-end
]

def create_application(route_list:list[APIRouter]) -> FastAPI: 
    application = FastAPI()

    for route in route_list: 
        application.include_router(route)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return application

app = create_application(route_list=route_list)

@app.get('/')
async def get_introduction(): 
    return {'message': "Welcome to B2M-BuildMyMuscle"}
    
if __name__ == "__main__":
    uvicorn.run("main:app", 
                host="127.0.0.1",
                port=8000, 
                reload=True
                )