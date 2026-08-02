from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
from database import get_db

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

# 1. 挑戦ログを新規投稿する
@app.post("/logs", response_model=schemas.ChallengeLogResponse)
def create_log(log_in: schemas.ChallengeLogCreate, db: Session = Depends(get_db)):
    # PydanticモデルからSQLAlchemyモデルオブジェクトを作成
    db_log = models.CompanionLog(**log_in.model_dump())
    
    db.add(db_log)       # DBに追加
    db.commit()          # 変更を確定
    db.refresh(db_log)   # 自動生成されたIDやタイムスタンプを取得
    return db_log

# 2. 全件取得する
@app.get("/logs", response_model=List[schemas.ChallengeLogResponse])
def get_logs(db: Session = Depends(get_db)):
    logs = db.query(models.CompanionLog).all()
    return logs

# 3. 週末に振り返りを記録する
@app.put("/logs/{log_id}", response_model=schemas.ChallengeLogResponse)
def update_log(log_id: int, log_update: schemas.ChallengeLogUpdate, db: Session = Depends(get_db)):
    # 該当のログを検索
    db_log = db.query(models.CompanionLog).filter(models.CompanionLog.id == log_id).first()
    if not db_log:
        raise HTTPException(status_code=404, detail="Log not found")
    
    # 送られてきた（Noneでない）値だけを更新
    update_data = log_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_log, key, value)
        
    db.commit()
    db.refresh(db_log)
    return db_log