import sqlite3
# Подключаем (или создаем, если файла нет) database
conn = sqlite3.connect("library.db") #database
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    year INTEGER,
    avaible INTEGER
)
                """)

conn.commit()



'''CRUD - Create Read Update Delete'''

books = [
    ("ГАрри потер", "KK.DK Linta", 2000, 1),
    ("SPonge Bob", "толкин", 1999, 1),
    ("Python for nubs", "Ivanov", 2026, 1),
    ("Physics", "Sokrat", 1981, 1)
]

cursor.executemany("INSERT INTO books (title, author, year, avaible) VALUES (?, ?, ?, ?)", books)
conn.commit()




#---------------------------READ (чтение данных)

print("\n=== Все books ===")
cursor.execute("SELECT * FROM books")
for row in cursor.fetchall():
    print(row)


print("\n=== Только имена ===")
cursor.execute("SELECT * FROM books WHERE avaible = 1")
for row in cursor.fetchall():
    print(row)


# # ------------------------ UPDATE (обновление данных) -----

cursor.execute("UPDATE books SET avaible = 0 WHERE id = 1")
conn.commit()



# print("\n=== После обновления ===")

cursor.execute("SELECT * FROM books")
for row in cursor.fetchall():
    print(row)


# ------------------------ DELETE (удаление данных)


cursor.execute("DELETE FROM books WHERE year < 2000")
conn.commit()

print("\n=== После удаления ===")
cursor.execute("SELECT * FROM books")
for row in cursor.fetchall():
    print(row)

# Закрываем соединение
conn.close()

