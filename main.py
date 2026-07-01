from database.user_repository import get_users


def main():

    users = get_users()

    for user in users:

        print(user)


if __name__ == "__main__":

    main()