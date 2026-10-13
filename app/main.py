from fastapi import FastAPI

app = FastAPI(
	title="TaskForge AAPI",
	description="A task management REST API",
	version="0.1.0",
)

@app.get("/")
def root():
	return {"message": "Welcome to TaskForge API"}

