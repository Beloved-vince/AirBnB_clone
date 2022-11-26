#!/usr/bin/python3
import pep8
import os
import unittest
from models.base_model import BaseModel
from models.place import Place
base = BaseModel()

class Test_place(unittest.TestCase):
    """Place class test"""
    @classmethod
    def setUpClass(cls):
        cls._place = Place()
        cls._place.city_id = "Betty"
        cls._place.user_id = "Vince"
        cls._place.name = "vinceoludare"
        cls._place.description = "test loading"
        cls._place.number_rooms = 0
        cls._place.number_bathrooms = 0
        cls._place.max_guest = 0
        cls._place.price_by_night = 0.0
        cls._place.latitude = 6.6
        cls._place.longitude = 0.12
        cls._place.amenity_ids = ["121", 123]



    @classmethod
    def tearDownClass(cls):
        del cls._place
        try:
            os.remove("file.json")
        except:
            pass

    def test_pep8_place(self):
        """Test for files  presents"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/place.py'])
        pass

    def test_place(self):
        """Place class attributes test"""
        self.assertTrue('city_id' in Place.__dict__)
        self.assertTrue("user_id" in Place.__dict__)
        self.assertTrue("name" in Place.__dict__)
        self.assertTrue("description" in Place.__dict__)
        self.assertTrue("number_rooms" in Place.__dict__)
        self.assertTrue("number_bathrooms" in Place.__dict__)
        self.assertTrue("max_guest" in Place.__dict__)
        self.assertTrue("price_by_night" in Place.__dict__)
        self.assertTrue("latitude" in Place.__dict__)
        self.assertTrue("longitude" in Place.__dict__)
        self.assertTrue("amenity_ids" in Place.__dict__)

    
    def test_place_class(self):
         """save Place details"""
         BaseModel.save(Place)
         self.assertNotEqual(base.created_at, BaseModel.save(Place))

    def test_place_type(self):
        """Test attribute data type"""
        self.assertTrue(type(Place.city_id), str)
        self.assertTrue(type(Place.user_id), str)
        self.assertTrue(type(Place.name), str)
        self.assertTrue(type(Place.description), str)
        self.assertTrue(type(Place.number_rooms), int)
        self.assertTrue(type(Place.number_bathrooms), int)
        self.assertTrue(type(Place.max_guest), int)
        self.assertTrue(type(Place.price_by_night), float)
        self.assertTrue(type(Place.latitude), float)
        self.assertTrue(type(Place.longitude), float)
        self.assertTrue(type(Place.amenity_ids), list)



    def test_instance(self):
        """test instance"""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_place_docs(self):
        """Documentation in the Place class"""
        Place.__doc__ is not None
    
if __name__ == "__main__":
    unittest.main()