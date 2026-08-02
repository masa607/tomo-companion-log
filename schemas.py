from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

# 共通ベース
class ChallengeLogBase(BaseModel):
    title: str
    background: Optional[str] = None
    goal: str
    action: str

# 1. 新規作成用
class ChallengeLogCreate(ChallengeLogBase):
    user_id: Optional[int] = None

# 2. 振り返り更新用
class ChallengeLogUpdate(BaseModel):
    achievement_rate: Optional[int] = None
    good_points: Optional[str] = None
    bad_points: Optional[str] = None

# 3. APIレスポンス用
class ChallengeLogResponse(ChallengeLogBase):
    id: int
    user_id: Optional[int] = None
    achievement_rate: Optional[int] = None
    good_points: Optional[str] = None
    bad_points: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)