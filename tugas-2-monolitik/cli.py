from domain.ports import Loader, Saver
from services.user_service import create_user


def main(loader: Loader, saver: Saver):
    name = input("Name: ")
    email = input("Email: ")

    try:
        user = create_user(name, email, loader, saver)
        print(f"User created: {user}")
    except ValueError as error:
        print(f"Error: {error}")
