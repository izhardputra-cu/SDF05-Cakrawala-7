from domain.ports import Loader, Saver
from domain.rules import validate_user


def create_user(name, email, loader: Loader, saver: Saver):
    users = loader()
    user = validate_user(name, email)

    if any(existing["email"] == user["email"] for existing in users):
        raise ValueError("Email already exists")

    user["id"] = len(users) + 1
    users.append(user)
    saver(users)

    return user


def list_users(loader: Loader):
    return loader()
