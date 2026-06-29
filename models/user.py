class User:

    def __init__(self, user_id, name, email):

        self.user_id = user_id
        self.name = name
        self.email = email

    def display(self):

        print("=" * 40)
        print(f"ID    : {self.user_id}")
        print(f"Name  : {self.name}")
        print(f"Email : {self.email}")
        print("=" * 40)
