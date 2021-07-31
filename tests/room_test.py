import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest("Bob")
        self.room = Room(1)
        self.song = Song("Umbrella", "Rihanna", "Pop")

    def test_room_has_number(self):
        self.assertEqual(1, self.room.number)

    def test_room_has_no_occupants(self):
        self.assertEqual([], self.room.occupants)

    def test_room_can_check_in_guest(self):
        self.room.check_in_guest(self.guest)
        self.assertIn(self.guest, self.room.occupants)

    def test_room_can_check_out_guest(self):
        self.room.check_in_guest(self.guest)
        self.room.check_out_guest(self.guest)
        self.assertNotIn(self.guest, self.room.occupants)