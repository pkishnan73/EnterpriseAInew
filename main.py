from app.welcome import display_message
from models.user import User


def main():
    display_message()

    user1 = User(
        1,
        "Rajesh Krishnan",
        "pkrishnan73@gmail.com"
    )

    user1.display()


if __name__ == "__main__":
    main()
