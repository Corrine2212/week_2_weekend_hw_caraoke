import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self) -> None:
        self.guest = Guest("Corrine Sing", "Unbreak My Heart")

    def test_guest_has_name(self):
        expected_result = "Corrine Sing"
        actual_result = self.guest.guest_name
        self.assertEqual(expected_result, actual_result)

    def test_guest_has_a_fave_song(self):
        expected_result = "Unbreak My Heart"
        actual_result = self.guest.fave
        self.assertEqual(expected_result, actual_result)

        
