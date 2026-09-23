import unittest

from domain.rules import validate_user


class UserRulesTest(unittest.TestCase):
    def test_validate_user_cleans_name_and_email(self):
        user = validate_user(" Alice ", "ALICE@example.com")

        self.assertEqual(
            user,
            {
                "name": "Alice",
                "email": "alice@example.com",
            },
        )

    def test_empty_name_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Name cannot be empty"):
            validate_user("   ", "alice@example.com")

    def test_invalid_email_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Invalid email"):
            validate_user("Alice", "invalid-email")


if __name__ == "__main__":
    unittest.main()
