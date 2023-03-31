import unittest
from classes.guest import Guest
from classes.room import Room

class TestGuest(unittest.TestCase):
    def setUp(self) -> None:
        self.guest = Guest("Corrine Sing", "Unbreak My Heart", 35)
        self.room1 = Room("Room 1", 10, 15)

    def test_guest_has_name(self):
        expected_result = "Corrine Sing"
        actual_result = self.guest.guest_name
        self.assertEqual(expected_result, actual_result)

    def test_guest_has_a_fave_song(self):
        expected_result = "Unbreak My Heart"
        actual_result = self.guest.fave_song
        self.assertEqual(expected_result, actual_result)

    def test_guest_has_funds_in_wallet(self):
        expected_result = 35
        actual_result = self.guest.wallet
        self.assertEqual(expected_result, actual_result)
        
    def test_guest_can_pay_room_fee(self):
        self.guest.pays_room_fee(self.room1)
        expected_result = 25 
        actual_result = self.guest.wallet
        self.assertEqual(expected_result, actual_result)

    # def test_guest_has_sufficient_funds_returns_true(self):


    


