from typing import Text
import unittest,robot,sys,os
from unittest.mock import patch
from io import StringIO


sys.stdout = open(os.devnull, "w")                #devnull indicates that a special file os.devnull will be used.
class create_robot_start(unittest.TestCase):
    @patch('sys.stdin', StringIO('HAL\n'))
    def test_robot_name(self):
        """test for input name"""
        toy_name = robot.robot_name()
        self.assertEqual(toy_name,'HAL')

    @patch('sys.stdin', StringIO('back 10\n'))
    def test_command_input(self):
        """test for input command"""
        toy_name = 'HAL'
        command = robot.get_input(toy_name)
        self.assertEqual(command,'back 10')

    def test_help_function(self):
        """ test help function"""
        output = robot.command_help()
        self.assertEqual(output,"""I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - moves the robot forward
BACK - moves the robot backward
RIGHT - moves the robot to the right
LEFT - moves the robot to the left
SPRINT - moves the robot faster and at a longer distance
    
""")
    def test_command_choice(self):
        """test the command choice"""
        toy_name= "HAL"
        command = "OFF"

        command_list = robot.command_choice(command,toy_name)
        self.assertTrue(command_list)

    def test_forward_function(self):
        """test forward function"""
        toy_name = 'HAL'
        value = 90
        move = 'FORWARD 10'
        steps = 10
        axis = (0,0)
        steps_taken = robot.forward_direction(toy_name,axis,value, steps)
        self.assertEqual(steps_taken,(0,10))


    def test_back_function(self):
        """test backward function"""
        toy_name = 'HAL'
        value = 90
        move = 'BACK 10'
        steps = 10
        axis = (0,0)
        steps_taken = robot.backward_direction(toy_name, value, axis,steps)
        self.assertEqual(steps_taken,(0,10))


    def test_right_function(self):
        """test turn right command"""
        toy_name = 'HAL'
        command = 'RIGHT'
        value = 90
        new_direction = robot.turn_right(toy_name, value)
        self.assertEqual(new_direction,0)


    def test_left_function(self):
        """test for turn left command"""
        toy_name = 'HAL'
        command = 'LEFT'
        value = 90
        new_direction = robot.turn_left(toy_name, value)
        self.assertEqual(new_direction,180)



    def test_direction_function(self):
        """test direction of the x,y,value and steps """
        command = 'FORWARD 10'
        x,y = (0,0)
        value = 90
        steps = 10
        direction = robot.direction(x, y, steps, value)
        self.assertEqual(direction,(0,10))


    def test_area_limit(self):
        """ test limit area of y value  """
        y = -200
        old_y = 200
        area =robot.area_limit_y(y,old_y)
        self.assertTrue(area)


    def test_area_limit(self):
        """ test limit area of x value """
        x = -200
        old_x = 200
        area =robot.area_limit_x(x,old_x)
        self.assertTrue(area)


if __name__ == '__main__':
    unittest.main()        