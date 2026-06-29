from database.connection import get_connection

def test_connection():
    try:
        conn = get_connection()
        print("✓ Database connection successful")
        
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        print(f"✓ PostgreSQL version: {version[0]}")
        
        cursor.close()
        conn.close()
        print("✓ Connection closed successfully")
        return True
    except Exception as e:
        print(f"✗ Connection failed: {e}")
        return False

if __name__ == "__main__":
    test_connection()
