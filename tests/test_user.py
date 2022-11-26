import pep8
import os
import unittest
from models.base_model import BaseModel
from models.user import User
base = BaseModel()


class Test_User(unittest.TestCase):
    """User class test"""
    @classmethod
    def setUpClass(cls):
        cls._user = User()
        cls._user.first_name = "Betty"
        cls._user.last_name = "Vince"
        cls._user.email = "vinceoludare@gmail.com"
        cls._user.password = "2324f"

    @classmethod
    def tearDownClass(cls):
        del cls._user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8_user(self):
        """Test for files  presents"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, 'check pep8')

    def test_user(self):
        """User class attributes test"""
        self.assertTrue('email' in User.__dict__)
        self.assertTrue("password" in User.__dict__)
        self.assertTrue("first_name" in User.__dict__)
        self.assertTrue("last_name" in User.__dict__)

    def test_user_class(self):
        """save user details"""
        BaseModel.save(User)
        self.assertNotEqual(base.created_at, BaseModel.save(User))

    def test_user_type(self):
        """Test attribute data type"""
        self.assertTrue(type(User.first_name), str)
        self.assertTrue(type(User.last_name), str)
        self.assertTrue(type(User.password), str)
        self.assertTrue(type(User.email), str)

    def test_instance(self):
        """test instance"""
        user = User()
        self.assertIsInstance(user, User)

    def test_user_docs(self):
        """Documentation in the user class"""
        User.__doc__ is not None


if __name__ == "__main__":
    unittest.main()
