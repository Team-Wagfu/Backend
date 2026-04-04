from fastapi import FastAPI
import routes as r

# initialise the app
app = FastAPI()

# include routers
app.include_router(r.dashboard_router)		# dashboard endpoints
app.include_router(r.pets_router)			# pet endpoints
app.include_router(r.vet_router)			# vet endpoints

# run the app
# use uvicorn main:app (refer README)