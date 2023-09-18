import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        tipo TEXT NOT NULL,
        id_turno_acesso INTEGER,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL,
        FOREIGN KEY (id_turno_acesso) REFERENCES turnos_acesso (id)
    )
''')

cursor.execute('''
               CREATE TABLE IF NOT EXIXTS turnos (
               id_turnos INTEGER PRIMARY KEY AUTOINCREMENT,
               turno DATETIME NOT NULL;
               )''')

conn.commit()
conn.close()
