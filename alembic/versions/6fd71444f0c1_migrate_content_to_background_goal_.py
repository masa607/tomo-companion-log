"""migrate_content_to_background_goal_action

Revision ID: 6fd71444f0c1
Revises: 2c38bdef53d2
Create Date: 2026-08-02 14:50:09.276362

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6fd71444f0c1'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1. 新規カラムを nullable=True で追加
    op.add_column('companion_logs', sa.Column('background', sa.Text(), nullable=True))
    op.add_column('companion_logs', sa.Column('goal', sa.Text(), nullable=True))
    op.add_column('companion_logs', sa.Column('action', sa.Text(), nullable=True))

    # 2. 既存の content データを background に移行＆未設定値を補填
    op.execute("UPDATE companion_logs SET background = content WHERE content IS NOT NULL")
    op.execute("UPDATE companion_logs SET goal = '未設定（自動移行）' WHERE goal IS NULL")
    op.execute("UPDATE companion_logs SET action = '未設定（自動移行）' WHERE action IS NULL")

    # 3. 必須指定（NOT NULL）に変更
    op.alter_column('companion_logs', 'goal', nullable=False)
    op.alter_column('companion_logs', 'action', nullable=False)

    # 4. 旧カラム content を削除
    op.drop_column('companion_logs', 'content')

def downgrade() -> None:
    # ロールバック用の処理
    op.add_column('companion_logs', sa.Column('content', sa.Text(), nullable=True))
    op.execute("UPDATE companion_logs SET content = background")
    op.drop_column('companion_logs', 'action')
    op.drop_column('companion_logs', 'goal')
    op.drop_column('companion_logs', 'background')
