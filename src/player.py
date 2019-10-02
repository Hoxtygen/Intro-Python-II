# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    """docstring for Player."""

    def __init__(self,name='Sub-zero', current_room='outside'):
        self.current_room = current_room

    def getCurrentRoom(self):
        return self.current_room

    def getName(self):
        return self.name
        
