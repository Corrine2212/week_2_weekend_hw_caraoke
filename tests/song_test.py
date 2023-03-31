import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Unbreak My Heart", "Toni Braxton")

    def test_song_has_a_title(self):
        self.assertEqual("Unbreak My Heart", self.song.song_title)

    def test_song_has_an_artist(self):
        self.assertEqual("Toni Braxton", self.song.artist)

