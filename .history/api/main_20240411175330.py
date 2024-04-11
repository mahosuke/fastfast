from fastapi import FastAPI

from api.routers import done, tasks

app = FastAPI()
app.include_router(tasks.router)
app.include_router(done.router)