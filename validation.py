# validation.py
from pydantic import BaseModel, validator

class ChapterValidation(BaseModel):
    content: str
    mood_score: float
    conflict_count: int
    
    @validator('mood_score')
    def check_mood_consistency(cls, v):
        if v < 0.7:
            raise ValueError("Mood consistency too low")
        return v