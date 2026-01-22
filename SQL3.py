import sqlite3
# Подключаем (или создаем, если файла нет) database
conn = sqlite3.connect("teachers.db") #database
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    subject TEXT,
    exprience INTEGER
)
                """)

conn.commit()



'''CRUD - Create Read Update Delete'''

cursor.execute("INSERT INTO teachers (name, subject, exprience) VALUES (?, ?, ?)",
               ("Азамат", "Матем", 5))

cursor.execute("INSERT INTO teachers (name, subject, exprience) VALUES (?, ?, ?)",
               ("Николай", "Биология", 11))

cursor.execute("INSERT INTO teachers (name, subject, exprience) VALUES (?, ?, ?)",
               ("Медина", "Алгебра", 20))

conn.commit()




#---------------------------READ (чтение данных)

print("\n=== Все учителя ===")
cursor.execute("SELECT * FROM teachers")
for row in cursor.fetchall():
    print(row)

# # ------------------------ UPDATE (обновление данных) -----

cursor.execute("UPDATE teachers SET exprience = exprience + 1 WHERE id = 3")
conn.commit()



# # print("\n=== После обновления ===")

cursor.execute("SELECT * FROM teachers")
for row in cursor.fetchall():
    print(row)


# ------------------------ DELETE (удаление данных)


cursor.execute("DELETE FROM teachers WHERE exprience = (SELECT MAX(exprience) FROM teachers)")
conn.commit()


print("\n=== После удаления ===")
cursor.execute("SELECT * FROM teachers")
for row in cursor.fetchall():
    print(row)

# # Закрываем соединение
conn.close()










