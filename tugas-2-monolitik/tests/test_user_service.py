import unittest

from services.user_service import create_user


class UserServiceTest(unittest.TestCase):
    def test_create_user_saves_user(self):
        saved_users = []

        def load_users():
            return []

        def save_users(updated_users):
            saved_users.extend(updated_users)

        user = create_user(" Alice ", "ALICE@example.com", load_users, save_users)

        self.assertEqual(user, {"name": "Alice", "email": "alice@example.com"})
        self.assertEqual(saved_users, [user])

    def test_create_user_rejects_invalid_name(self):
        def load_users():
            return []

        with self.assertRaisesRegex(ValueError, "Name cannot be empty"):
            create_user("   ", "alice@example.com", load_users, lambda users: None)


if __name__ == "__main__":
    unittest.main()
