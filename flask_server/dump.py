from sqlalchemy import create_engine
engine = create_engine('sqlite:///./sqlitedb.db', echo=True)

conn = engine.raw_connection()
with open('./dump.sql', 'w') as f:
    for line in conn.iterdump():
        f.write('%s\n' % line)