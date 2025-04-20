import psycopg2
import csv

def connect():
    return psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="mar.hanym2007!"
    )

# Вставка или обновление одного пользователя
def insert_or_update(name, phone):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
        conn.commit()
        print(f"Inserted or updated: {name}")
    except Exception as e:
        print("Error in insert_or_update:", e)
    finally:
        cur.close()
        conn.close()

# Поиск по шаблону
def search_pattern(pattern):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM search_phonebook(%s)", (pattern,))
        rows = cur.fetchall()
        print("Search results:")
        for row in rows:
            print(row)
    except Exception as e:
        print("Error in search_pattern:", e)
    finally:
        cur.close()
        conn.close()

# Массовая вставка
def insert_many(users):
    try:
        conn = connect()
        cur = conn.cursor()
        formatted = "ARRAY[" + ", ".join(
            "ARRAY['{}','{}']".format(
                u[0].replace("'", "''"), u[1].replace("'", "''")
            ) for u in users
        ) + "]"

        sql = f"CALL insert_many_users({formatted}::TEXT[][])"
        cur.execute(sql)
        conn.commit()
        print("Bulk insert executed.")
    except Exception as e:
        print("Error in insert_many:", e)
    finally:
        cur.close()
        conn.close()

# Загрузка пользователей из csv-файла
def insert_from_csv(file_path):
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            users = []
            for row in reader:
                if len(row) == 2:
                    name = row[0].strip()
                    phone = row[1].strip()
                    users.append([name, phone])
            insert_many(users)
    except Exception as e:
        print("CSV read error:", e)

# Запуск
if __name__ == '__main__':
    insert_or_update("Alice", "+7474567890")

    search_pattern("Ali")

    # Массовая вставка из списка
    users = [
        ['Bob', '1234567890'],
        ['Charlie', 'abcdef'],
        ['David', '9876543210'],
        ['Eve', '12345']
    ]
    insert_many(users)
    insert_from_csv('a.csv')
