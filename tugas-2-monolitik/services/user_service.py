from domain.rules import validate_user


def create_user(name, email, load_users, save_users):
    user = validate_user(name, email)
    users = load_users()
    users.append(user)
    save_users(users)
    return user
