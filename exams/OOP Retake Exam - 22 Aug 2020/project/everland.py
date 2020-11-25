from project.people.child import Child
from project.rooms.room import Room


class Everland:
    rooms: list

    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        expenses = sum([room.expenses + room.room_cost for room in self.rooms])
        return f"Monthly consumptions: {expenses:.2f}$."

    def pay(self):
        res = ""
        rooms_to_remove = []
        for i_room, room in enumerate(self.rooms):
            payment = room.expenses + room.room_cost
            if payment > room.budget:
                rooms_to_remove.append(room)
            res += f"{str(room)}"
        for room in rooms_to_remove:
            self.rooms.pop(rooms_to_remove.index(room))
        return res.rstrip()

    def status(self):
        all_people_in_hotel = sum([room.members_count for room in self.rooms])
        res = f"Total population: {all_people_in_hotel}\n"
        for room in self.rooms:
            res += f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n"
            if len(room.children) > 0:
                res += "\n".join(f"--- Child {n} monthly cost: {child.cost * 30:.2f}$" for n, child in enumerate(room.children)) + "\n"
            res += f"--- Appliances monthly cost: {room.expenses:.2f}$\n"
        return res
