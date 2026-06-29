from database.user_repository import insert_user

def main():

    insert_user(
        "Anita",
        "anita@gmail.com",
        "Manager"
    )

    print("User Inserted")

if __name__ == "__main__":

    main()
