class Room:
    def __init__(self, room_name, fee, room_size):
        self.room_name = room_name
        self.room_fee = fee
        self.song_list = []
        self.guest_list = []
        self.room_size = room_size


    def song_count(self):
        return len(self.song_list)

    def add_song_to_room(self, song_to_add):
        self.song_list.append(song_to_add)

    def guest_count(self):
        return len(self.guest_list)

    def check_in_guests(self, guest_to_add):
        if self.guest_count() < self.room_size:
            self.guest_list.append(guest_to_add)
            return True
        else:
            return False
            
    def check_out_guests(self, guest_to_remove):
        self.guest_list.remove(guest_to_remove)        
       
# - Guests could have a favourite song, and if their favourite song is on the room's playlist, they can cheer loudly! (return a string like "Whoo!")
# - Rooms can keep track of the entry fees/spending of the guests - maybe add a bar tab/bar class?
# - Add anything extra you think would be good to have at a karaoke venue!    