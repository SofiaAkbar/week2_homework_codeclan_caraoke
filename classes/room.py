class Room:
    
    def __init__(self, number):
        self.number = number
        self.occupants = []
        
    def check_in_guest(self, guest):
        self.occupants.append(guest)

    def check_out_guest(self, guest):
        self.occupants.remove(guest)