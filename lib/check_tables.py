from sqlalchemy import create_engine, inspect
from models import Base

# Connect to the database
engine = create_engine("sqlite:///freebies.db")  # Change if using PostgreSQL
inspector = inspect(engine)

# Get the list of tables
print(inspector.get_table_names())  # Expected output: ['companies', 'devs', 'freebies']
