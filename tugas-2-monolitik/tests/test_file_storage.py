import tempfile
import unittest
from pathlib import Path

from adapters.file_storage import load_users, save_users


class FileStorageTest(unittest.TestCase):
    def test_load_users_returns_empty_list_when_file_does_not_exist(self):
        with tempfile.TemporaryDirectory() as temp_directory:
            path = Path(temp_directory) / "users.json"

            self.assertEqual(load_users(path), [])

    def test_saved_users_can_be_loaded_again(self):
        users = [{"id": 1, "name": "Alice", "email": "alice@example.com"}]

        with tempfile.TemporaryDirectory() as temp_directory:
            path = Path(temp_directory) / "users.json"

            save_users(users, path)

            self.assertEqual(load_users(path), users)


if __name__ == "__main__":
    unittest.main()
