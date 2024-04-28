__author__="Minh Le"
__version__="0.0.0"

import logging
import uvicorn

from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse
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
    try: 
        content = """Hi there! I am here you help you to achieve for fitness goals. \n
                   I can help you with: \n
                        1. Scheduling a week workout plan for you. \n
                        2. Figuring out your perfect meal plans that match your fitness goals. \n
                        3. Guiding you to use appropriate supplements."""
        return JSONResponse(content=content,
                            status_code=200)
    except: 
        return JSONResponse(content="Something is broken from the server.\n \
                            Please! Contact me via minh.leduc.0210@gmail.com for more support", 
                            status_code=404)
    
if __name__ == "__main__":
    uvicorn.run("main:app", 
                host="127.0.0.1",
                port=8000, 
                reload=True
                )