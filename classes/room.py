class Room:
    
    def __init__(self, number):
        self.number = number
        self.occupants = []
        self.playing_song = None
        
    def check_in_guest(self, guest):
        self.occupants.append(guest)

    def check_out_guest(self, guest):
        self.occupants.remove(guest)

    def play_song(self, song):
        self.playing_song = song