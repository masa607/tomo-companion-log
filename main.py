from fastapi import FastAPI, HTTPException
from data import ChallengeLogCreate, ChallengeLogUpdate

app = FastAPI()

db_logs = []

@app.get("/")
def read_root():
    return {"message": "Hello World"}

#挑戦ログを新規投稿する
@app.post("/logs")
def create_log(log_in: ChallengeLogCreate):
    # 送られてきたデータを、扱いやすいように辞書型に変換する
    log_data = log_in.model_dump()
    
    # あとで更新や特定ができるように、仮のIDと、振り返りの初期値を追加する
    log_data["id"] = len(db_logs) + 1
    # 新規投稿時は振り返りはまだ無いので空にする
    log_data["reflection"] = ""  
    
    # 仮のデータベース（リスト）に保存
    db_logs.append(log_data)
    return log_data

#きちんと更新されているのか確認するため、全件取得する
@app.get("/logs")
def get_logs():
    return db_logs