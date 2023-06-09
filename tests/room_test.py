import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("Room 1", 10, 15)
        self.song_1 = Song("Unbreak My Heart", "Toni Braxton")
        self.guest_1 = Guest("Corrine Sing", "Unbreak My Heart", 35)
        self.guest_2 = Guest("Theo Sing", "Boss Bitch", 20)
        self.guest_3 = Guest("George Bacon", "Rather Be", 15)
        
    def test_room_has_name(self):
        expected_value = "Room 1"
        actual_value = self.room1.room_name
        self.assertEqual(expected_value, actual_value)

    def test_room_has_fee(self):
        expected_value = 10
        actual_value = self.room1.room_fee
        self.assertEqual(expected_value, actual_value)

    def test_room_can_add_songs(self):
        self.room1.add_song_to_room(self.song_1)
        self.assertEqual(1, self.room1.song_count())

    def test_room_can_check_guests_in(self):
        self.room1.check_in_guests(self.guest_1)
        self.assertEqual(1, self.room1.guest_count())

    def test_room_can_check_guests_out(self):
        self.room1.check_in_guests(self.guest_1)
        self.room1.check_out_guests(self.guest_1)
        self.assertEqual(0, self.room1.guest_count())

    def test_room_can_limit_number_of_guests(self):
        self.room2 = Room("Room 2", 5, 2)
        self.assertEqual(True, self.room2.check_in_guests(self.guest_1))
        self.assertEqual(True, self.room2.check_in_guests(self.guest_2))
        self.assertEqual(False, self.room2.check_in_guests(self.guest_3))




