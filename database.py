import os
from sqlalchemy import create_engine
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
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()