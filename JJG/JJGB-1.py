import random

class DungeonMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = [["#" for _ in range(width)] for _ in range(height)]
    
    def generate(self, room_attempts=20, room_min_size=3, room_max_size=7):
        rooms = []
        
        for _ in range(room_attempts):
            w = random.randint(room_min_size, room_max_size)
            h = random.randint(room_min_size, room_max_size)
            x = random.randint(1, self.width - w - 1)
            y = random.randint(1, self.height - h - 1)
            
            new_room = RectRoom(x, y, w, h)
            
            # Check if this room overlaps with any other
            if any(new_room.intersects(other_room) for other_room in rooms):
                continue  # skip to next attempt if overlap occurs
            
            # If no overlaps, add the room to the list
            rooms.append(new_room)
            self.create_room(new_room)
            
            # Connect with previous room
            if len(rooms) > 1:
                prev_x, prev_y = rooms[-2].center()
                new_x, new_y = new_room.center()
                self.create_corridor(prev_x, prev_y, new_x, new_y)
        
        # Start point in first room and exit in the last room
        self.start = rooms[0].center()
        self.end = rooms[-1].center()
        self.map[self.start[1]][self.start[0]] = "S"
        self.map[self.end[1]][self.end[0]] = "E"
    
    def create_room(self, room):
        for x in range(room.x1, room.x2):
            for y in range(room.y1, room.y2):
                self.map[y][x] = "."
    
    def create_corridor(self, x1, y1, x2, y2):
        if random.choice([True, False]):
            self.horizontal_tunnel(x1, x2, y1)
            self.vertical_tunnel(y1, y2, x2)
        else:
            self.vertical_tunnel(y1, y2, x1)
            self.horizontal_tunnel(x1, x2, y2)
    
    def horizontal_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.map[y][x] = "."
    
    def vertical_tunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.map[y][x] = "."
    
    def display(self):
        for row in self.map:
            print("".join(row))

class RectRoom:
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h

    def center(self):
        center_x = (self.x1 + self.x2) // 2
        center_y = (self.y1 + self.y2) // 2
        return center_x, center_y

    def intersects(self, other):
        return (
            self.x1 <= other.x2 and self.x2 >= other.x1 and
            self.y1 <= other.y2 and self.y2 >= other.y1
        )

# Parâmetros do mapa
map_width = 30
map_height = 20

# Criação do mapa e geração da dungeon
dungeon = DungeonMap(map_width, map_height)
dungeon.generate()
dungeon.display()

