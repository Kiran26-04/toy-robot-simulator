from robot import Robot, Facing

def extracting_place_command(cmd):
    parts = cmd.split()
    if len(parts) != 2:
        return None
    
    values = parts[1].split(',')
    if len(values) != 3:
        return None
    
    x = int(values[0])
    y = int(values[0])

    direction_name = values[2].upper()
    direction = Facing[direction_name]

    return x, y, direction

def main():

    robot = Robot()
    print("Welcome to the Toy Robot Simulator")

    while True:
        pass



