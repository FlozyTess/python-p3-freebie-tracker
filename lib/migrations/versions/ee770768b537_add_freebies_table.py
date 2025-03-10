"""Add freebies table

Revision ID: ee770768b537
Revises: 5f72c58bf48c
Create Date: 2025-03-10 11:11:08.455047

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee770768b537'
down_revision = '5f72c58bf48c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Apply the upgrade: Create the freebies table and modify the companies table."""
    
    # Create freebies table
    op.create_table(
        'freebies',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('item_name', sa.String(), nullable=False),
        sa.Column('value', sa.Integer(), nullable=False),
        sa.Column('dev_id', sa.Integer(), sa.ForeignKey('devs.id'), nullable=True),
        sa.Column('company_id', sa.Integer(), sa.ForeignKey('companies.id'), nullable=True),
    )
    
    with op.batch_alter_table('companies') as batch_op:
        batch_op.alter_column('name', existing_type=sa.VARCHAR(), nullable=False)
        batch_op.alter_column('founding_year', existing_type=sa.INTEGER(), nullable=False)


def downgrade() -> None:
    """Revert the changes: Drop the freebies table and modify the companies table back."""
    
    # Restore companies table columns to previous state
    with op.batch_alter_table('companies') as batch_op:
        batch_op.alter_column('founding_year', existing_type=sa.INTEGER(), nullable=True)
        batch_op.alter_column('name', existing_type=sa.VARCHAR(), nullable=True)
    
    # Drop freebies table
    op.drop_table('freebies')
