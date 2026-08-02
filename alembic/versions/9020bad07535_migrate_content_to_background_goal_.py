"""migrate_content_to_background_goal_action

Revision ID: 9020bad07535
Revises: 6fd71444f0c1
Create Date: 2026-08-02 14:59:44.735754

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9020bad07535'
down_revision: Union[str, Sequence[str], None] = '6fd71444f0c1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
