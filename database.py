import os
from sqlalchemy import create_engine
<<<<<<< HEAD
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# .env ファイルから環境変数を読み込む
load_dotenv()

# .env から DB 接続情報を取得
# 例: mysql+pymysql://ユーザー名:パスワード@ホスト名:ポート/データベース名
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://root:password@localhost:3306/tomobanso_db"
)

# SQLAlchemy エンジンの作成
engine = create_engine(
    DATABASE_URL,
    echo=True  # 実行されるSQLをターミナルに表示
)

# データベースセッションの作成
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# モデルの親クラス
Base = declarative_base()

# DBセッションを取得・終了するための依存関係関数
=======
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

>>>>>>> 620a18b3b821c67f6482127a9c42e59acbb0a65f
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
<<<<<<< HEAD
        db.close()
=======
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
>>>>>>> 620a18b3b821c67f6482127a9c42e59acbb0a65f
