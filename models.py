from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from database import Base

class CompanionLog(Base):
    __tablename__ = "companion_logs"

    id = Column(Integer, primary_key=True, index=True)
    #将来のユーザー機能のために、とりあえず nullable=True で定義しておく
    user_id = Column(Integer, index=True, nullable=True) 
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    achievement_rate = Column(Integer, nullable=True) # 達成度
    good_points = Column(Text, nullable=True)          # 良かったこと
    bad_points = Column(Text, nullable=True)  # 悪かったこと・改善点
    
    # 将来のユーザー機能用（一旦、空で許可）
    user_id = Column(Integer, index=True, nullable=True)

    # タイムスタンプ
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)