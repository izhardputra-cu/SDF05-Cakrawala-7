import unittest
from unittest.mock import patch

from cli import main


class CliTest(unittest.TestCase):
    @patch("builtins.print")
    @patch("builtins.input", side_effect=[" Budi ", "BUDI@example.com"])
    def test_main_uses_storage_given_by_the_application(self, _, mock_print):
        users = []

        def loader():
            return users

        def saver(updated_users):
            users[:] = updated_users

        main(loader, saver)

        self.assertEqual(users[0]["email"], "budi@example.com")
        mock_print.assert_called_once_with(
            "User created: {'name': 'Budi', 'email': 'budi@example.com', 'id': 1}"
        )


if __name__ == "__main__":
    unittest.main()
