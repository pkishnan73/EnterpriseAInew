import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from database.user_repository import (
    insert_user,
    get_users,
    update_user,
    delete_user
)

# Uncomment one operation at a time to test it.

# insert_user("Anita", "anita@gmail.com", "Manager")

# update_user(1, "Super Admin")

# delete_user(3)

users = get_users()

for user in users:
    print(user)