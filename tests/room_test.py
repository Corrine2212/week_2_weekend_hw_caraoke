import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Room 1", 10)
        self.song_1 = Song("Unbreak My Heart", "Toni Braxton")
        self.guest_1 = Guest("Corrine Sing", "Unbreak My Heart")
        self.guest_2 = Guest("Theo Sing", "Boss Bitch")
        
    def test_room_has_name(self):
        expected_value = "Room 1"
        actual_value = self.room.room_name
        self.assertEqual(expected_value, actual_value)

    def test_room_has_fee(self):
        expected_value = 10
        actual_value = self.room.room_fee
        self.assertEqual(expected_value, actual_value)

    def test_room_can_add_songs(self):
        self.room.add_song_to_room(self.song_1)
        self.assertEqual(1, self.room.song_count())

    def test_room_can_check_guests_in(self):
        self.room.check_in_guests(self.guest_1)
        self.assertEqual(1, self.room.guest_count())

    def test_room_can_check_guests_out(self):
        self.room.check_in_guests(self.guest_1)
        self.room.check_out_guests(self.guest_1)
        self.assertEqual(0, self.room.guest_count())

