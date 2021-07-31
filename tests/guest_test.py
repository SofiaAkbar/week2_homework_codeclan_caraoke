import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Bob")
        self.room = Room(1)
        self.song = Song("Umbrella", "Rihanna", "Pop")

    def test_guest_has_name(self):
        self.assertEqual("Bob", self.guest.name)