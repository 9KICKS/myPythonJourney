import unittest

from animal import Animal


class TestAnimalClass(unittest.TestCase):
    animal = Animal("name", "Yoruba", "100 mile", "20 km")

    def test_animal_name(self):
        self.animal.set_animal_name("Snopy")
        result = self.animal.get_animal_name()
        self.assertEquals("Snopy", result)

    def test_animal_move(self):
        self.animal.set_animal_move("20 km")
        result = self.animal.get_animal_move()
        self.assertTrue("20 km", result)

    def test_that_array_exist(self):
        animal_type_array = self.animal.get_animal_types()
        self.assertListEqual()
