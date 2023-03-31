class Room:
    def __init__(self, room_name, fee):
        self.room_name = room_name
        self.room_fee = fee
        self.song_list = []
        self.guest_counter = []

    def song_count(self):
        return len(self.song_list)

    def add_song_to_room(self, song_to_add):
        self.song_list.append(song_to_add)

    def guest_count(self):
        return len(self.guest_counter)

    def check_in_guests(self, guest_to_add):
        self.guest_counter.append(guest_to_add)

    def check_out_guests(self, guest_to_remove):
        self.guest_counter.remove(guest_to_remove)
       
        
    