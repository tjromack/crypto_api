import sqlite3

def setup_database():
    conn = sqlite3.connect('crypto_prices.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY,
            average_price REAL
        )
    ''')
    conn.commit()
    conn.close()

def save_to_database(average_price):
    conn = sqlite3.connect('crypto_prices.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO prices (average_price) VALUES (?)', (average_price,))
    conn.commit()
    conn.close()
