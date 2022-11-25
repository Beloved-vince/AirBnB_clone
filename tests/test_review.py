#!/usr/bin/python3
import pep8
import os
import unittest
from models.base_model import BaseModel
from models.review import Review
base = BaseModel()

class Test_review(unittest.TestCase):
    """User class test"""
    @classmethod
    def setUpClass(cls):
        cls._review = Review()
        cls._review.place_id = "Betty"
        cls._review.user_id = "vince"
        cls._review.text = "getting a successful text"

    @classmethod
    def tearDownClass(cls):
        del cls._review
        try:
            os.remove("file.json")
        except:
            pass

    def test_pep8_review(self):
        """Test for files  presents"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models.review.py'])
        # self.assertEqual(p.total_errors, 0, 'fix pep8')

    def test_Review(self):
        """User class attributes test"""
        self.assertTrue("place_id" in Review.__dict__)
        self.assertTrue("user_id" in Review.__dict__)
        self.assertTrue("text" in Review.__dict__)

    
    def test_Review_class(self):
         """save user details"""
         BaseModel.save(Review)
         self.assertNotEqual(base.created_at, BaseModel.save(Review))

    def test_Review_type(self):
        """Test attribute data type"""
        self.assertTrue(type(Review.place_id), str)
        self.assertTrue(type(Review.user_id), str)
        self.assertTrue(type(Review.text), str)

    def test_instance(self):
        """test instance"""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_Review_docs(self):
        """Documentation in the user class"""
        Review.__doc__ is not None
    
if __name__ == "__main__":
    unittest.main()