import pytest
from robot import Robot, Facing

def test_place():
    robot = Robot()
    robot.place(2,3,Facing.NORTH)
    assert robot.x == 2
    assert robot.y == 3
    assert robot.direction == Facing.NORTH
    assert robot.placed is True

def test_sequence():
    robot = Robot()
    robot.place(1,3,Facing.NORTH)
    robot.move()
    output = robot.report()
    assert output == "1,4,NORTH"

def test_cmd_without_place():
    robot = Robot()
    robot.move()    # can be any command
    assert robot.x is None
    assert robot.y is None
    assert robot.placed is False

def test_left_rotation():
    robot = Robot()
    robot.place(1,3,Facing.NORTH)
    robot.left()
    assert robot.direction == Facing.WEST

def test_clockwise_rotation():
    robot = Robot()
    robot.place(1,3,Facing.NORTH)
    for _ in range(4):
        robot.right()
    assert robot.direction == Facing.NORTH

def test_right_rotation():
    robot = Robot()
    robot.place(1,3,Facing.NORTH)
    robot.right()
    assert robot.direction == Facing.EAST

def test_anticlockwise_rotation():
    robot = Robot()
    robot.place(1,3,Facing.NORTH)
    for _ in range(4):
        robot.left()
    assert robot.direction == Facing.NORTH

def test_invalid_placement():
    robot = Robot()
    robot.place(5,5,Facing.NORTH)   # taking the default grid size (5x5)
    assert robot.x is None
    assert robot.y is None
    assert robot.placed is False

def test_place_after_place():
    robot = Robot()
    robot.place(1,2,Facing.NORTH)
    robot.move()
    robot.place(2,3,Facing.WEST)
    output = robot.report()
    assert output == "2,3,WEST"

def test_move_off_edge():
    robot = Robot()
    robot.place(2,0,Facing.SOUTH)   # can be done for EAST, WEST, NORTH
    robot.move()
    assert robot.x == 2
    assert robot.y == 0

def test_custom_grid_size():
    robot = Robot(width = 6, height = 6)
    robot.place(5,5,Facing.SOUTH)
    assert robot.x == 5
    assert robot.y == 5
    assert robot.placed is True
    robot.move()
    assert robot.y == 4
    



