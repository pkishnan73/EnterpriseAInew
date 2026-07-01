from database.connection import get_connection


def insert_user(name, email, role):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users(name, email, role)
        VALUES(%s, %s, %s)
        """,
        (name, email, role)
    )

    conn.commit()

    cursor.close()
    conn.close()


def get_users():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows


def update_user(user_id, role):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE users
        SET role = %s
        WHERE user_id = %s
        """,
        (role, user_id)
    )

    conn.commit()

    cursor.close()
    conn.close()


def delete_user(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM users
        WHERE user_id = %s
        """,
        (user_id,)
    )

    conn.commit()

    cursor.close()
    conn.close()


def update_user(user_id, role):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE users
        SET role = %s
        WHERE user_id = %s
        """,
        (role, user_id)
    )

    conn.commit()

    cursor.close()
    conn.close()


def delete_user(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM users
        WHERE user_id = %s
        """,
        (user_id,)
    )

    conn.commit()

    cursor.close()
    conn.close()