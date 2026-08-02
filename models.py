from sqlalchemy import Column, Integer, String, Text, DateTime, func
from base import Base

class CompanionLog(Base):
    __tablename__ = "companion_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True, nullable=True)

    title = Column(String(255), nullable=False)        # 追加: タイトル（必須）
    background = Column(Text, nullable=True)          # 背景（任意）
    goal = Column(Text, nullable=False)                # 目標（必須）
    action = Column(Text, nullable=False)              # アクション（必須）

    achievement_rate = Column(Integer, nullable=True)  # 達成度
    good_points = Column(Text, nullable=True)         # 良かった点
    bad_points = Column(Text, nullable=True)          # 悪かった点・改善点

    # サーバー（DB）側で自動生成するタイムスタンプ
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())