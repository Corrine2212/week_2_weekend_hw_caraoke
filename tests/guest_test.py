import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self) -> None:
        self.guest_1 = Guest("Corrine Sing", "Unbreak My Heart", 35)
        self.guest_2 = Guest("Theo Sing", "Boss Bitch", 20)
        self.guest_3 = Guest("George Bacon", "Rather Be", 15)
        self.room_1 = Room("Room 1", 10, 15)
        self.song_1 = Song("Unbreak My Heart", "Toni Braxton")
        self.song_2 = Song("Boss Bitch", "Doja Cat")


    def test_guest_has_name(self):
        expected_result = "Corrine Sing"
        actual_result = self.guest_1.guest_name
        self.assertEqual(expected_result, actual_result)

    def test_guest_has_a_fave_song(self):
        expected_result = "Unbreak My Heart"
        actual_result = self.guest_1.fave_song
        self.assertEqual(expected_result, actual_result)

    def test_guest_has_funds_in_wallet(self):
        expected_result = 35
        actual_result = self.guest_1.wallet
        self.assertEqual(expected_result, actual_result)
        
    def test_guest_can_pay_room_fee(self):
        self.guest_1.pays_room_fee(self.room_1)
        expected_result = 25 
        actual_result = self.guest_1.wallet
        self.assertEqual(expected_result, actual_result)


    def test_check_if_room_playlist_has_favourite_song(self):
        self.room_1.add_song_to_room(self.song_1)
        self.room_1.check_in_guests(self.guest_1)
        expected_result = "Wooooo!"
        actual_result = self.guest_1.check_if_room_playlist_has_favourite_song(self.room_1)
        self.assertEqual(expected_result, actual_result)



    # def test_guest_has_sufficient_funds_returns_true(self):


    


