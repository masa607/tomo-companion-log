from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from database import Base

# 1. 新規作成用（目標設定）
class ChallengeLogCreate(BaseModel):
    title: str
    background: str
    goal: str
    action: str

# 2. 週末の振り返り更新用（達成度・良かったこと・悪かったこと）
class ChallengeLogUpdate(BaseModel):
    achievement_rate: Optional[int] = None # 例: 80 (80%)
    good_points: Optional[str] = None     # 良かったこと
    bad_points: Optional[str] = None      # 悪かったこと・改善点

# 3. APIからのレスポンス用
class ChallengeLogResponse(ChallengeLogCreate):
    id: int
    achievement_rate: Optional[int] = None
    good_points: Optional[str] = None
    bad_points: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True