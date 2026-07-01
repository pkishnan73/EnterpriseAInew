import sys
from pathlib import Path

from sqlalchemy.orm import Session

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from models.user import User


class UserRepository:

    #########################################
    # CREATE
    #########################################

    def create_user(
        self,
        db: Session,
        name,
        email,
        role
    ):

        user = User(
            name=name,
            email=email,
            role=role
        )

        db.add(user)

        db.commit()

        db.refresh(user)

        return user


    #########################################
    # READ ALL
    #########################################

    def get_all_users(
        self,
        db: Session
    ):

        return db.query(User).all()


    #########################################
    # READ BY ID
    #########################################

    def get_user_by_id(
        self,
        db: Session,
        user_id
    ):

        return db.query(User).filter(
            User.user_id == user_id
        ).first()


    #########################################
    # UPDATE
    #########################################

    def update_user(
        self,
        db: Session,
        user_id,
        name,
        email,
        role
    ):

        user = db.query(User).filter(
            User.user_id == user_id
        ).first()

        if user:

            user.name = name
            user.email = email
            user.role = role

            db.commit()

            db.refresh(user)

        return user


    #########################################
    # DELETE
    #########################################

    def delete_user(
        self,
        db: Session,
        user_id
    ):

        user = db.query(User).filter(
            User.user_id == user_id
        ).first()

        if user:

            db.delete(user)

            db.commit()

        return user