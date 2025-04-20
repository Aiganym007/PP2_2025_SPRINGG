#in snake_db, create a function dekete_scores_for_user(username) that deletes scores of a user with the specified username

import psycopg2
def get_connection():
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="mar.hanym2007!",
        host="localhost",
        port="5432"
    )

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) UNIQUE
    )
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS user_score (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        score INTEGER,
        level INTEGER,
        saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    conn.commit()
    cur.close()
    conn.close()

def get_user(username):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user

def create_user(username):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users(username) VALUES (%s) RETURNING id", (username,))
    user_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return user_id

def get_user_progress(user_id):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT score, level FROM user_score
            WHERE user_id = %s
            ORDER BY saved_at DESC
            LIMIT 1
        """, (user_id,))
        result = cur.fetchone()
        cur.close()
        conn.close()
        return result
    except Exception as e:
        print("Ошибка при загрузке прогресса:", e)
        return None
    
def delete_scores_for_user(username):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE scores FROM user_score WHERE user_id = '4' ")
    conn.commit()
    cur.close()
    conn.close()


def save_progress(user_id, score, level):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO user_score(user_id, score, level) VALUES (%s, %s, %s)", (user_id, score, level))
    conn.commit()
    cur.close()
    conn.close()



