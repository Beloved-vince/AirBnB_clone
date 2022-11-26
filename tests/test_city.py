#!/usr/bin/python3
import pep8
import os
import unittest
from models.base_model import BaseModel
from models.city import City
base = BaseModel()


class Test_User(unittest.TestCase):
    """User class test"""
    @classmethod
    def setUpClass(cls):
        cls._user = City()
        cls._user.name = "Betty"
        cls._user.state_id = "Vince"

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
        p = style.check_files(['models.city.py'])
        # self.assertEqual(p.total_errors, 0, 'fix pep8')

    def test_city(self):
        """User class attributes test"""
        self.assertTrue("name" in City.__dict__)
        self.assertTrue("state_id" in City.__dict__)

    def test_city_class(self):
        """save user details"""
        BaseModel.save(City)
        self.assertNotEqual(base.created_at, BaseModel.save(City))

    def test_city_type(self):
        """Test attribute data type"""
        self.assertTrue(type(City.state_id), str)
        self.assertTrue(type(City.name), str)

    def test_instance(self):
        """test instance"""
        city = City()
        self.assertIsInstance(city, City)

    def test_city_docs(self):
        """Documentation in the user class"""
        City.__doc__ is not None


if __name__ == "__main__":
    unittest.main()
