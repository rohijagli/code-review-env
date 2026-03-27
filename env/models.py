from pydantic import BaseModel
from typing import List

class Observation(BaseModel):
    code: str
    difficulty: str

class Action(BaseModel):
    issues: List[str]
    explanation: str
    severity: str   # "low", "medium", "high"
    fix: str

class Reward(BaseModel):
    score: float