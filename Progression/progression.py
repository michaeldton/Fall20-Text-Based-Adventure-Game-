from Room.room import Room
from Player.player import Player
from Inventory.inventory import Inventory
from Item.item import Item


class Progression:

    @staticmethod
    def perform_interaction(item, player_inventory, room):

        if item == "tree branch" and room.name == "Serene Forest - North":
            for obj in room.inventory.get_inventory_list():
                if obj.name == "Rusted Key":
                    print("debug")
                    obj.toggle_obtainable()
                    room.room_drop_item("rusted key", player_inventory)
                    break

            # room.room_drop_item(item)
            # player.player_add_item(item)

        else:
            print("Not a valid interaction.")
