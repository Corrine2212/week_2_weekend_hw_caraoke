class Guest:
    def __init__(self,name,fave_song, wallet):
        self.guest_name = name
        self.fave_song = fave_song
        self.wallet = wallet

    def pays_room_fee(self, room):
        self.wallet -= room.room_fee

    def check_if_room_playlist_has_favourite_song(self, room):
        # check if the guest's fave song is in the room's playlist 
        # if true return "Wooooo!"
        # if false return "That sucks"
        for song in room.song_list:
            if song.song_title == self.fave_song:
                return "Wooooo!"
        return "That sucks"
                