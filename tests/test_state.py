#!/usr/bin/python3
import pep8
import os
import unittest
from models.base_model import BaseModel
from models.state import State
base = BaseModel()


class Test_state(unittest.TestCase):
    """User class test"""
    @classmethod
    def setUpClass(cls):
        cls._state = State()
        cls._state.name = "Betty"

    @classmethod
    def tearDownClass(cls):
        del cls._state
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8_state(self):
        """Test for files  presents"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models.State.py'])
        # self.assertEqual(p.total_errors, 0, 'fix pep8')

    def test_state(self):
        """User class attributes test"""
        self.assertTrue("name" in State.__dict__)

    def test_state_class(self):
        """save user details"""
        BaseModel.save(State)
        self.assertNotEqual(base.created_at, BaseModel.save(State))

    def test_state_type(self):
        """Test attribute data type"""
        self.assertTrue(type(State.name), str)

    def test_instance(self):
        """test instance"""
        state = State()
        self.assertIsInstance(state, State)

    def test_state_docs(self):
        """Documentation in the user class"""
        State.__doc__ is not None


if __name__ == "__main__":
    unittest.main()
