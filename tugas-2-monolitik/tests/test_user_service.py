import unittest

from services.user_service import create_user, list_users


class UserServiceTest(unittest.TestCase):
    def test_create_user_uses_storage_contract(self):
        users = []

        def loader():
            return users

        def saver(updated_users):
            users[:] = updated_users

        user = create_user(" Bob ", "BOB@example.com", loader, saver)

        self.assertEqual(user["id"], 1)
        self.assertEqual(users[0]["email"], "bob@example.com")

    def test_duplicate_email_is_rejected(self):
        users = [{"id": 1, "name": "Alice", "email": "alice@example.com"}]

        with self.assertRaisesRegex(ValueError, "Email already exists"):
            create_user(
                "Another Alice",
                "ALICE@example.com",
                lambda: users,
                lambda _: None,
            )

    def test_list_users_uses_loader(self):
        users = [{"id": 1, "name": "Alice", "email": "alice@example.com"}]

        self.assertEqual(list_users(lambda: users), users)


if __name__ == "__main__":
    unittest.main()
