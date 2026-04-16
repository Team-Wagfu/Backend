from fastapi import FastAPI

from .routes import petRouter, testRouter

app = FastAPI(
	title="Wagfu",
	description="Pet care and emergency response system",
	version="0.0.1",
)

app.include_router(petRouter)
app.include_router(testRouter)
print('[Starting server]')

# run the app