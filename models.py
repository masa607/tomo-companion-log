from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from base import Base  

class CompanionLog(Base):
    __tablename__ = "companion_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True, nullable=True)

    title = Column(String(255), nullable=False)
    background = Column(Text, nullable=True)
    goal = Column(Text, nullable=False)
    action = Column(Text, nullable=False)

    achievement_rate = Column(Integer, nullable=True)
    good_points = Column(Text, nullable=True)
    bad_points = Column(Text, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())