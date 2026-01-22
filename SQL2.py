# import sqlite3
# # Подключаем (или создаем, если файла нет) database
# conn = sqlite3.connect("shop.db") #database
# cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS products (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     price INTEGER,
#     category TEXT
# )
#                 """)

# conn.commit()



# '''CRUD - Create Read Update Delete'''

# cursor.execute("INSERT INTO products (name, price, category) VALUES (?, ?, ?)",
#                ("Яблоко", 100, "Фрукты"))

# cursor.execute("INSERT INTO products (name, price, category) VALUES (?, ?, ?)",
#                ("Помидор", 50, "Овощи"))

# cursor.execute("INSERT INTO products (name, price, category) VALUES (?, ?, ?)",
#                ("Сгущенка", 10, "Молочные"))

# conn.commit()




# print("\n=== Все ===")
# cursor.execute("SELECT * FROM products")
# for row in cursor.fetchall():
#     print(row)



# print("\n=== Только имена ===")
# cursor.execute("SELECT name FROM products")
# for row in cursor.fetchall():
#     print(row[0])



# cursor.execute("UPDATE products SET price = 20 WHERE name = 'Яблоко'")
# conn.commit()

# print("\n=== После обновления ===")

# cursor.execute("SELECT * FROM products")
# for row in cursor.fetchall():
#     print(row)

# ################################################


# cursor.execute("DELETE FROM products WHERE name = 'Помидор'")
# conn.commit()

# print("\n=== После удаления ===")
# cursor.execute("SELECT * FROM products")
# for row in cursor.fetchall():
#     print(row)

# # Закрываем соединение
# conn.close()








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
               ("Студент", 14, "azamat@example.com"))

cursor.execute("INSERT INTO students (name, age, email) VALUES (?, ?, ?)",
               ("Ученик", 16, "malika@example.com"))

conn.commit()



# print("\n=== Все студенты ===")
# cursor.execute("SELECT * FROM students")
# for row in cursor.fetchall():
#     print(row)


print("\n=== Только имена ===")
cursor.execute("SELECT name FROM students")
for row in cursor.fetchall():
    print(row[0])

print("\n Больше 15 лет")
cursor.execute("SELECT * FROM students WHERE age > 15")
for row in cursor.fetchall():
    print(row)

print("\n конкретное имя")
cursor.execute("SELECT name FROM students WHERE name = 'Студент'")
for row in cursor.fetchall():
    print(row)





cursor.execute("UPDATE students SET age = 18 WHERE name = 'Ученик'")
conn.commit()


cursor.execute("UPDATE students SET email = 'posty@example.com' WHERE name = 'Студент'")
conn.commit()


# print("\n=== После обновления ===")

cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)


# # ------------------------ DELETE (удаление данных)


cursor.execute("DELETE FROM students WHERE age < 15")
conn.commit()

print("\n=== После удаления ===")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

# Закрываем соединение
conn.close()




