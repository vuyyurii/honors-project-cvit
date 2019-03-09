import sqlite3

conn = sqlite3.connect('../../second/db.sqlite3')
print("Opened database successfully")

a = ('meetings',)

conn.execute("INSERT INTO meetings_meeting (name,tim,meetingpath,transcript,words) \
      VALUES (?, 'time', 'meetingpath', 'transcript', 'words')", a);

conn.commit()
print("Records created successfully")

conn.close()