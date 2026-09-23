import json
from pathlib import Path


def load_users(path="users.json"):
    file_path = Path(path)

    if not file_path.exists():
        return []

    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_users(users, path="users.json"):
    with Path(path).open("w", encoding="utf-8") as file:
        json.dump(users, file, indent=2)
