# Toy Robot Code Challenge
This Python console application is a simulation of a toy robot moving on a square table top, of dimensions 5 units x 5 units.

## Given facts
* There are no other obstructions on the table surface.
* The robot is free to roam around the surface of the table.
* Any movement that would result in the robot falling from the table must be prevented, however further valid movement commands must still be allowed.

## Description

### Given Commands and their meanings
    * PLACE
        * `PLACE X, Y, F` - PLACE will put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST.
        * The origin (0,0) can be considered to be the SOUTH WEST most corner.
        * It is required that the first command to the robot is a `PLACE` command, after that, any sequence of commands may be issued, in any order, including another `PLACE` command. The application should discard all commands in the sequence until a valid `PLACE` command has been executed.

    * MOVE
        * `MOVE` will move the toy robot one unit forward in the direction it is currently facing.

    * LEFT and RIGHT
        * `LEFT` and `RIGHT` will rotate the robot 90 degrees in the specified direction **without** changing the position of the robot.

    * REPORT
        * `REPORT` will announce the X,Y and F of the robot.

* A robot that is not on the table can choose to ignore the `MOVE`, `LEFT`, `RIGHT` and `REPORT` commands.
* Input can be from a file, or from standard input. In this application, we will use standard input and use `EXIT` to quit the simulator.

## Constraints
* The toy robot must not fall off the table during movement - This also includes the initial placement of the toy robot.
* Any move that would cause the robot to fall must be ignored - something like 'Violates constraint' will be printed on the console.


## Example Input and Output:

#### a --------

    PLACE 0,0,NORTH
    MOVE
    REPORT

Expected output: 0,1,NORTH

#### b --------

    PLACE 0,0,NORTH
    LEFT
    REPORT

Expected output: 0,0,WEST

#### c --------

    PLACE 1,2,EAST
    MOVE
    MOVE
    LEFT
    MOVE
    REPORT

Expected output: 3,3,NORTH

## SETUP:
