from typing import Optional

from pydantic import BaseModel, Field

class TaskCreate(BaseModel):
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    done: bool = Field(False, description="完了フラグ")

    
