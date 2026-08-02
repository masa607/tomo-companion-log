import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from base import Base 

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

if __name__ == "__main__":
    import models  

    print("--- 登録されているテーブル確認 ---")
    print(Base.metadata.tables.keys())

    print("既存のテーブルを削除しています...")
    Base.metadata.drop_all(bind=engine)

    print("新しいテーブルを作成しています...")
    Base.metadata.create_all(bind=engine)

    print("テーブルの初期化・再作成が完了しました！")