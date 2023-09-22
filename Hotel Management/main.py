class Hotel:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.total_rooms = []

    def add_new_room(self, name, num_of_beds, fare_per_day):
        self.total_rooms.append({
            "hotel_name": self.name,
            "room_name": name,
            "num_of_beds": num_of_beds,
            "fare_per_day": fare_per_day,
            "dateOccupy": {} 
        })

    def book_a_room(self, name, user, date):
        for room in self.total_rooms:
            if room["room_name"] == name:
                if date in room["dateOccupy"]:
                    print(f"Room '{name}' is not available on {date}")
                else:
                    room["dateOccupy"][date] = user
                    print(f"Room '{name}' booked for {user} on {date}")
                break
        else:
            print(f"Room '{name}' not found")

    def view_stats(self):
        total_rooms = len(self.total_rooms)
        occupied_rooms = sum(1 for room in self.total_rooms if room["dateOccupy"])
        available_rooms = total_rooms - occupied_rooms

        print(f"Total rooms: {total_rooms},occupied: {occupied_rooms},available: {available_rooms}")
    

    def is_available(self, name, date):
        for room in self.total_rooms:
            if room["room_name"] == name:
                if date in room["dateOccupy"]:
                    print(f"Room '{name}' is not available on {date}")
                else:
                    print(f"Room '{name}' is available on {date}")
                break
        else:
            print(f"Room '{name}' not found")

# hotel = Hotel("MYHOTEL", "ABC")

# hotel.add_new_room("Single", 1, 100)
# hotel.is_available("Single", "2023-09-25") 
# hotel.book_a_room("Single", "Jane Smith", "2023-09-24")

# hotel.add_new_room("Family", 6, 150)
# hotel.book_a_room("Single", "John Doe", "2023-09-23")
# hotel.is_available("Family", "2023-09-25") 

# hotel.view_stats()

