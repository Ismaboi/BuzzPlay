import sqlite3

DB_FILE = "buzzplay.db"

def initialize_database():
    """Initialize the database and create required tables."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()

        # Create users table (if not exists)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
        """)

        # Create messages table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender TEXT NOT NULL,
            receiver TEXT NOT NULL,
            message TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)

        conn.commit()

# ✅ Function to save a user
def save_user(username, password):
    """Save a new user in the database."""
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
    except sqlite3.IntegrityError:
        raise ValueError("Username already exists!")

# ✅ Function to retrieve a user
def get_user(username):
    """Retrieve user details from the database."""
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
            return cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None

# ✅ Function to send a message
def send_message(sender, receiver, message):
    """Save a new message in the database."""
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO messages (sender, receiver, message) VALUES (?, ?, ?)", 
                           (sender, receiver, message))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")

# ✅ Function to retrieve messages between two users
def get_messages(user1, user2):
    """Retrieve chat history between two users."""
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT sender, message, timestamp FROM messages
            WHERE (sender = ? AND receiver = ?) OR (sender = ? AND receiver = ?)
            ORDER BY timestamp
            """, (user1, user2, user2, user1))
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []

# Initialize database when the script runs
initialize_database()
