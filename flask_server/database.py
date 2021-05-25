from sqlalchemy import create_engine
engine = create_engine('sqlite:///./sqlitedb.db', echo=True)
engine.execute('CREATE TABLE table_test(test int)')
