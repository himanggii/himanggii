import sqlite3

def vulnerable_sql():
    conn = sqlite3.connect('vulnerable.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    username = input("Enter username: ")  # Unsanitized input
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)  # Vulnerable to SQL injection
    print(cursor.fetchall())
    conn.close()

if __name__ == "__main__":
    vulnerable_sql()
