import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest("Bob")
        self.room = Room(1)
        self.song = Song("Umbrella", "Rihanna", "Pop")

    def test_song_has_title(self):
        self.assertEqual("Umbrella", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("Rihanna", self.song.artist)

    def test_song_has_genre(self):
        self.assertEqual("Pop", self.song.genre)