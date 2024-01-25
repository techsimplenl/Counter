from sqlalchemy import create_engine, MetaData

def check_if_table_exists(path):
    # Replace 'your_database_url' with the actual URL of your SQLite database.
    engine = create_engine(path)
    metadata = MetaData()

    # Reflect the existing tables in the database
    metadata.reflect(bind=engine)

    # Check if the 'counter' table exists and drop it if it does
    if 'counter' in metadata.tables:
        metadata.tables['counter'].drop()

    # Now create the 'counter' table again
    # (Add your table creation code here)
