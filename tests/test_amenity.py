#!/usr/bin/python3
import pep8
import os
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
base = BaseModel()


class Test_amenity(unittest.TestCase):
    """User class test"""
    @classmethod
    def setUpClass(cls):
        cls._amenity = Amenity()
        cls._amenity.name = "Betty"

    @classmethod
    def tearDownClass(cls):
        del cls._amenity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8_amenity(self):
        """Test for files  presents"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models.amenity.py'])
        # self.assertEqual(p.total_errors, 0, 'fix pep8')

    def test_Amenity(self):
        """User class attributes test"""
        self.assertTrue("name" in Amenity.__dict__)

    def test_Amenity_class(self):
        """save user details"""
        BaseModel.save(Amenity)
        self.assertNotEqual(base.created_at, BaseModel.save(Amenity))

    def test_Amenity_type(self):
        """Test attribute data type"""
        self.assertTrue(type(Amenity.name), str)

    def test_instance(self):
        """test instance"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_Amenity_docs(self):
        """Documentation in the user class"""
        Amenity.__doc__ is not None


if __name__ == "__main__":
    unittest.main()
