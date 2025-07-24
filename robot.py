from enum import Enum

class Facing(Enum): # have to follow an order (currently clockwise)
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Robot:
    def __init__(self, width = 5, height = 5):
        self.x = None       # not placed yet
        self.y = None
        self.direction = None
        self.placed = False
        self.width = width
        self.height = height
    
    def valid_position(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height
    
    def place(self, x, y, direction): # only places if the position is valid
        if self.valid_position(x, y) and direction in Facing:
            self.x = x
            self.y = y
            self.direction = direction
            self.placed = True
        else:
            print('Command ignored!')
    
    def move(self): #moves 1 unit forward + moves only if the position after that 1 unit is valid
        if not self.placed:
            print("Oops! Robot hasn't been placed yet. Use the PLACE command first")
            return
        new_x, new_y = self.x, self.y
        if self.direction == Facing.NORTH:
            new_y +=1
        elif self.direction == Facing.SOUTH:
            new_y -=1
        elif self.direction == Facing.EAST:
            new_x +=1
        elif self.direction == Facing.WEST:
            new_x -=1
        
        if self.valid_position(new_x, new_y):
            self.x = new_x      #updating the final position
            self.y = new_y
        else:
            print('Command ignored!')
    
    def left(self):
        if self.placed:
            self.direction = Facing((self.direction.value-1)%4)
        else:
            print("Oops! Robot hasn't been placed yet. Use the PLACE command first")
            return

    
    def right(self):
        if self.placed:
            self.direction = Facing((self.direction.value+1)%4)
        else:
            print("Oops! Robot hasn't been placed yet. Use the PLACE command first")
            return
    
    def report(self):
        if self.placed:
            return f'{self.x},{self.y},{self.direction.name}'
        print('Oops! Robot needs to be placed first to report the position. Use the PLACE command first')
        return None
    
