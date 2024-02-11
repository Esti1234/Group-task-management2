from fastapi import APIRouter

tasks = APIRouter(responses={404: {"description": "not found"}})
demo_tasks = {
    1: {"task_name": "Complete Python tutorial", "completed": False},
    2: {"task_name": "Read documentation on FastAPI", "completed": False},
    3: {"task_name": "Develop a sample FastAPI application", "completed": False},
    4: {"task_name": "Explore Uvicorn server options", "completed": False},
    5: {"task_name": "Write unit tests for the application", "completed": False},
    6: {"task_name": "Review asyncio concepts", "completed": False},
    7: {"task_name": "Experiment with async HTTP clients", "completed": False},
    8: {"task_name": "Deploy application to a cloud service", "completed": False},
    9: {"task_name": "Monitor application performance", "completed": False},
    10: {"task_name": "Gather feedback from users", "completed": False},
}


@tasks.get("/tasks/")
def get_tasks():
    return demo_tasks
