import sqlite3
# Подключаем (или создаем, если файла нет) database
conn = sqlite3.connect("school.db") #database
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT
)
                """)

conn.commit()




'''CRUD - Create Read Update Delete'''

cursor.execute("INSERT INTO students (name, age, email) VALUES (?, ?, ?)",
               ("Азамат", 14, "azamat@example.com"))

cursor.execute("INSERT INTO students (name, age, email) VALUES (?, ?, ?)",
               ("Малика", 16, "malika@example.com"))

cursor.execute("INSERT INTO students (name, age, email) VALUES (?, ?, ?)",
               ("Медина", 17, "medina@example.com"))
conn.commit()




#---------------------------READ (чтение данных)

print("\n=== Все студенты ===")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

print("\n=== Только имена ===")
cursor.execute("SELECT name FROM students")
for row in cursor.fetchall():
    print(row[0])


# # ------------------------ UPDATE (обновление данных) -----

cursor.execute("UPDATE students SET age = 18 WHERE name = 'Нур'")
conn.commit()



# print("\n=== После обновления ===")

cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)


# ------------------------ DELETE (удаление данных)


cursor.execute("DELETE FROM students WHERE name = 'Азамат'")
conn.commit()

print("\n=== После удаления ===")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

# Закрываем соединение
conn.close()

