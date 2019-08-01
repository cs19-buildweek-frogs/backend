# from django.contrib.auth.models import User
# from adventure.models import Player, Room


# Room.objects.all().delete()

# r_outside = Room(title="Outside Cave Entrance",
#                description="North of you, the cave mount beckons", x=1, y=0, id=0)

# r_foyer = Room(title="Foyer", description="""Dim light filters in from the south. Dusty
# passages run north and east.""", x=1, y=1, id=1)

# r_overlook = Room(title="Grand Overlook", description="""A steep cliff appears before you, falling
# into the darkness. Ahead to the north, a light flickers in
# the distance, but there is no way across the chasm.""", x=1, y=2, id=2)

# r_narrow = Room(title="Narrow Passage", description="""The narrow passage bends here from west
# to north. The smell of gold permeates the air.""", x=0, y=1,  id=3)

# r_treasure = Room(title="Treasure Chamber", description="""You've found the long-lost treasure
# chamber! Sadly, it has already been completely emptied by
# earlier adventurers. The only exit is to the south.""", x=0, y=2, id=4)

# r_outside.save()
# r_foyer.save()
# r_overlook.save()
# r_narrow.save()
# r_treasure.save()

# # Link rooms together
# r_outside.connectRooms(r_foyer, "n")
# r_foyer.connectRooms(r_outside, "s")

# r_foyer.connectRooms(r_overlook, "n")
# r_overlook.connectRooms(r_foyer, "s")

# r_foyer.connectRooms(r_narrow, "e")
# r_narrow.connectRooms(r_foyer, "w")

# r_narrow.connectRooms(r_treasure, "n")
# r_treasure.connectRooms(r_narrow, "s")


# players=Player.objects.all()
# for p in players:
#   p.currentRoom=r_outside.id
#   p.save()

from django.contrib.auth.models import User
from adventure.models import Player, Room


Room.objects.all().delete()

room_list = [
    {
        "id": 0,
        "x": 2,
        "y": 2,
        "title": "Room 0",
        "n": 1,
        "s": 3,
        "e": 4,
        "w": 2,
        "description": "There are exits to the north south east west",
        "items": [""]
    },
    {
        "id": 1,
        "x": 2,
        "y": 3,
        "title": "Room 1",
        "n": 6,
        "s": 1,
        "e": 5,
        "w": -1,
        "description": "There are exits to the north south east",
        "items": [""]
    },
    {
        "id": 2,
        "x": 4,
        "y": 2,
        "title": "Room 2",
        "n": 7,
        "s": 8,
        "e": 0,
        "w": -1,
        "description": "There are exits to the north south east",
        "items": [""]
    },
    {
        "id": 3,
        "x": 2,
        "y": 0,
        "title": "Room 3",
        "n": 0,
        "s": -1,
        "e": 9,
        "w": 8,
        "description": "There are exits to the north east west",
        "items": [""]
    },
    {
        "id": 4,
        "x": 0,
        "y": 2,
        "title": "Room 4",
        "n": 5,
        "s": 10,
        "e": -1,
        "w": 0,
        "description": "There are exits to the north south west",
        "items": [""]
    },
    {
        "id": 5,
        "x": 0,
        "y": 3,
        "title": "Room 5",
        "n": 11,
        "s": 4,
        "e": -1,
        "w": 1,
        "description": "There are exits to the north south west",
        "items": [""]
    },

    {
        "id": 6,
        "x": 2,
        "y": 4,
        "title": "Room 6",
        "n": -1,
        "s": 1,
        "e": 15,
        "w": 7,
        "description": "There are exits to the south east west",
        "items": [""]
    },
    {
        "id": 7,
        "x": 4,
        "y": 4,
        "title": "Room 7",
        "n": 14,
        "s": 2,
        "e": 6,
        "w": -1,
        "description": "There are exits to the north south east",
        "items": [""]
    },
    {
        "id": 8,
        "x": 4,
        "y": 0,
        "title": "Room 8",
        "n": 2,
        "s": -1,
        "e": 3,
        "w": -1,
        "description": "There are exits to the north east",
        "items": [""]
    },
    {
        "id": 9,
        "x": 0,
        "y": 0,
        "title": "Room 9",
        "n": 10,
        "s": -1,
        "e": -1,
        "w": 3,
        "description": "There are exits to the north west",
        "items": [""]
    },
    {
        "id": 10,
        "x": 0,
        "y": 1,
        "title": "Room 10",
        "n": 4,
        "s": 9,
        "e": -1,
        "w": -1,
        "description": "There are exits to the north south",
        "items": [""]
    },

    {
        "id": 11,
        "x": 0,
        "y": 4,
        "title": "Room 11",
        "n": 13,
        "s": 5,
        "e": -1,
        "w": 15,
        "description": "There are exits to the north south west",
        "items": [""]
    },
    {
        "id": 12,
        "x": 2,
        "y": 5,
        "title": "Room 12",
        "n": -1,
        "s": 6,
        "e": 13,
        "w": 14,
        "description": "There are exits to the south east west",
        "items": [""]
    },
    {
        "id": 13,
        "x": 0,
        "y": 5,
        "title": "Room 13",
        "n": -1,
        "s": 11,
        "e": -1,
        "w": 12,
        "description": "There are exits to the south west",
        "items": [""]
    },
    {
        "id": 14,
        "x": 4,
        "y": 5,
        "title": "Room 14",
        "n": -1,
        "s": 7,
        "e": 12,
        "w": 16,
        "description": "There are exits to the south east west",
        "items": [""]
    },
    {
        "id": 15,
        "x": 1,
        "y": 4,
        "title": "Room 15",
        "n": -1,
        "s": -1,
        "e": 11,
        "w": 6,
        "description": "There are exits to the east west",
        "items": [""]
    },

    {
        "id": 16,
        "x": 5,
        "y": 5,
        "title": "Room 16",
        "n": -1,
        "s": 17,
        "e": 14,
        "w": -1,
        "description": "There are exits to the south east",
        "items": [""]
    },
    {
        "id": 17,
        "x": 5,
        "y": 4,
        "title": "Room 17",
        "n": 16,
        "s": 18,
        "e": -1,
        "w": -1,
        "description": "There are exits to the north south",
        "items": [""]
    },
    {
        "id": 18,
        "x": 5,
        "y": 2,
        "title": "Room 18",
        "n": 17,
        "s": 19,
        "e": -1,
        "w": -1,
        "description": "There are exits to the north south",
        "items": ["dragon"]
    },
    {
        "id": 19,
        "x": 5,
        "y": 0,
        "title": "Room 19",
        "n": 18,
        "s": -1,
        "e": 8,
        "w": -1,
        "description": "There are exits to the north east",
        "items": [""]
    },
    {
        "id": 20,
        "x": 3,
        "y": 3,
        "title": "Room 20",
        "n": -1,
        "s": -1,
        "e": 1,
        "w": -1,
        "description": "There is exit to the east",
        "items": [""]
    }
]

for r in room_list:
    n = r["n"] if "n" in r else -1
    s = r["s"] if "s" in r else -1
    e = r["e"] if "e" in r else -1
    w = r["w"] if "w" in r else -1
    if "x" in r:
        x = r["x"]
    if "y" in r:
        y = r["y"]
    # make_r = Room(id=r["id"], title=r["title"],
    #               description=r["description"], x=x, y=y, n=n, s=s, e=e, w=w)
    make_r = Room(id=r["id"], title=r["title"], description=r["description"], x=x, y=y, n=n, s=s, e=e, w=w,
                  items="".join(r["items"]))
    make_r.save()

players = Player.objects.all()
for p in players:
    p.currentRoom = r_outside.id
    p.save()
