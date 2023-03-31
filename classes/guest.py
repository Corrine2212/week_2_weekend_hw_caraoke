class Guest:
    def __init__(self,name,fave_song, wallet):
        self.guest_name = name
        self.fave_song = fave_song
        self.wallet = wallet

    def pays_room_fee(self, room):
        self.wallet -= room.room_fee
        