import uvicorn
from fastapi import FastAPI

from tasks_route import tasks

app = FastAPI()

app.include_router(tasks)

uvicorn.run(app, host="127.0.0.1", port=3001)