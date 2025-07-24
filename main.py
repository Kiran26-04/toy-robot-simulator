from robot import Robot, Facing

def extracting_place_command(cmd):
    try:
        parts = cmd.split()
        if len(parts) != 2:
            print('Invalid format of the PLACE command! Please use the format - PLACE X,Y,DIRECTION and try again')
            return None
        
        values = parts[1].split(',')
        if len(values) != 3:
            print('Invalid format of the PLACE command! Please use the format - PLACE X,Y,DIRECTION. Try again!')
            return None
        
        x = int(values[0])
        y = int(values[1])

        direction_name = values[2].upper()
        direction = Facing[direction_name]      # handle KeyError

        return x, y, direction
    except ValueError:
        print('Invalid x and y coordinates. Please enter non-negative integers. Try again!')
        return None
    except KeyError:
        print('Invalid direction. Choose from NORTH, SOUTH, EAST, WEST. Try again!')

def main():

    print("Welcome to the Toy Robot Simulator")
    print("You'll now be asked to enter the dimensions of the table (width & height)")
    try:
        width = int(input('Enter the width of table (default is 5): ') or 5)
    except ValueError:
        print('Invalid width! Taking the default width as 5')
        width = 5
    
    try:
        height = int(input('Enter the height of table (default is 5): ') or 5)
    except ValueError:
        print('Invalid height! Taking the default height as 5')
        height = 5
    
    robot = Robot(width = width, height = height)


    while True:
        cmd = input('>>>> ').strip().upper()
        if cmd == 'EXIT':
            print('Exiting the simulator...')
            break

        elif cmd.startswith('PLACE'):
            output = extracting_place_command(cmd)
            if output:
                x, y, direction = output
                robot.place(x, y, direction)
        elif cmd == 'MOVE':
            robot.move()
        elif cmd == 'LEFT':
            robot.left()
        elif cmd == 'RIGHT':
            robot.right()
        elif cmd == 'REPORT':
            report_output = robot.report()
            if report_output:
                print('Output:', report_output)
        else:
            print('The following command does not exist. Choose from PLACE, MOVE, RIGHT, LEFT, REPORT. Try again!')

if __name__ == "__main__":
    main()


