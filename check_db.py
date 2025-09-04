import sqlite3

conn = sqlite3.connect('admin.db')
cur = conn.cursor()
cur.execute('SELECT name FROM sqlite_master WHERE type="table"')
tables = [row[0] for row in cur.fetchall()]
print('Current tables:', tables)

# Check if current_file table exists
if 'current_file' in tables:
    cur.execute('SELECT * FROM current_file')
    rows = cur.fetchall()
    print('Current file records:', rows)
else:
    print('current_file table does not exist yet')

conn.close()
