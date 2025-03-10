"""create db

Revision ID: 7a71dbf71c64
Revises: 
Create Date: 2023-03-15 15:05:55.516631

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a71dbf71c64'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create 'freebies' table
    op.create_table(
        'freebies',
        sa.Column('id', sa.Integer, primary_key=True),   # Unique ID for each freebie
        sa.Column('item_name', sa.String, nullable=False),  # Name of the freebie
        sa.Column('value', sa.Integer, nullable=False),  # Freebie value
        sa.Column('dev_id', sa.Integer, sa.ForeignKey('devs.id'), nullable=False),  # Link to the Dev table
        sa.Column('company_id', sa.Integer, sa.ForeignKey('companies.id'), nullable=False)  # Link to the Company table
     )
    


def downgrade() -> None:
    # Drop 'freebies' table if rolling back
    op.drop_table('freebies')  
    
