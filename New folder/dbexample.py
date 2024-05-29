import sqlite3

con=sqlite3.connect('samp.db')
print(con)
#con.execute('''create table avi(name text,salary real,mob integer)''')
#con.execute('''update avi set name="shiva" where name="shankar"''')
#con.execute(''' delete from avi where name="prince" ''')
a=con.execute('''select * from avi''')
print(a.fetchmany())
con.commit()
con.close()
