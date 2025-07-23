from robot import Robot, Facing

def extracting_place_command(cmd):
    try:
        parts = cmd.split()
        if len(parts) != 2:
            print('Invalid format!')
            return None
        
        values = parts[1].split(',')
        if len(values) != 3:
            print('Invalid format!')
            return None
        
        x = int(values[0])
        y = int(values[1])

        direction_name = values[2].upper()
        direction = Facing[direction_name]      #handle KeyError

        return x, y, direction
    except (ValueError, KeyError):
        print('Invalid PLACE command. Please check the format!')
        return None

def main():

    # robot = Robot()
    print("Welcome to the Toy Robot Simulator")
    try:
        width = int(input('Enter the width of table (default is 5): ') or 5)
        height = int(input('Enter the height of table (default is 5): ') or 5)

    except ValueError:
        print('Invalid grid size!')
        width = 5
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
            print('The following command does not exist.')

if __name__ == "__main__":
    main()


