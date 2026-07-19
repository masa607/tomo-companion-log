from pydantic import BaseModel
from typing import Optional

#１.挑戦を新しく投稿する時のデータの形
class ChallengeLogCreate(BaseModel):
    title: str
    background: str
    goal: str
    action: str

#2.週末に振り返りを更新する時のデータの形
class ChallengeLogUpdate(BaseModel):
    reflection: str