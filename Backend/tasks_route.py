from fastapi import APIRouter

tasks = APIRouter(responses={404: {"description": "not found"}})


@tasks.get("/tasks/")
def get_tasks():
    return {"message": "all tasks"}
