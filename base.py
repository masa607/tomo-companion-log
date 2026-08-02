from sqlalchemy.orm import declarative_base

# Baseの二重生成・循環参照を防ぐための独立ファイル
Base = declarative_base()