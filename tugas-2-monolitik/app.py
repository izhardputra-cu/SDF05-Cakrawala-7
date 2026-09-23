from functools import partial
from pathlib import Path

from adapters.file_storage import load_users, save_users
from cli import main


if __name__ == "__main__":
    users_path = Path(__file__).with_name("users.json")
    loader = partial(load_users, users_path)
    saver = partial(save_users, path=users_path)

    main(loader, saver)
