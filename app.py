from fastapi import FastAPI
from src.router import get_routes

app = FastAPI()



api_routes = get_routes()
for api_route in api_routes:
	app.include_router(api_route)

