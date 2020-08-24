import psycopg2

connection = psycopg2.connect('dbname=sandwich user=postgres password=balto')

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table2;')

cursor.execute('''
    CREATE TABLE table2(
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')

cursor.execute('INSERT INTO table2 (id, completed) VALUES (1, true);')

cursor.execute('INSERT INTO table2 (id, completed)' + 'VALUES (%(id)s, %(completed)s);', {
    'id': 2,
    'completed': False
})

cursor.execute('SELECT * from table2;')

result = cursor.fetchall()
print(result)

connection.commit()

connection.close()
cursor.close()
