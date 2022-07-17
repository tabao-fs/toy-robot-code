import unittest
from unittest.mock import patch
from main import run_robot


class TestRobot(unittest.TestCase):

    @patch('builtins.input')
    def test_place_1(self, inp):
        inp.side_effect = ['PLACE 0,0,NORTH', 'MOVE', 'REPORT']
        res = run_robot()
        self.assertEqual('0,1,NORTH', res)

    @patch('builtins.input')
    def test_place_2(self, inp):
        inp.side_effect = ['PLACE 0,0,NORTH', 'LEFT', 'REPORT']
        res = run_robot()
        self.assertEqual('0,0,WEST', res)

    @patch('builtins.input')
    def test_place_3(self, inp):
        inp.side_effect = [
            'PLACE 1,2,EAST', 'MOVE', 'MOVE', 'LEFT', 'MOVE', 'REPORT']
        res = run_robot()
        self.assertEqual('3,3,NORTH', res)

    @patch('builtins.input')
    def test_place_table_edge(self, inp):
        inp.side_effect = ['PLACE 0,0,WEST', 'MOVE', 'REPORT']
        res = run_robot()
        self.assertEqual('0,0,WEST', res)

    @patch('builtins.input')
    def test_ignore_before_place(self, inp):
        inp.side_effect = ['REPORT', 'MOVE', 'LEFT', 'RIGHT', 'PLACE 0,0,NORTH', 'MOVE', 'REPORT']
        res = run_robot()
        self.assertEqual('0,1,NORTH', res)

    @patch('builtins.input')
    def test_place_commands(self, inp):
        inp.side_effect = ['PLACE 0,0,NORTH', 'PLACE 1,2,EAST', 'REPORT']
        res = run_robot()
        self.assertEqual('1,2,EAST', res)

    @patch('builtins.input')
    def test_wrong_place_command(self, inp):
        inp.side_effect = ['PLACE 0,0,NORTH', 'PLACE 5,5,NORTH', 'REPORT']
        res = run_robot()
        self.assertEqual('0,0,NORTH', res)

    @patch('builtins.input')
    def test_ignore_wrong_move_command(self, inp):
        inp.side_effect = ['PLACE 0,0,NORTH', 'MOV', 'REPORT']
        res = run_robot()
        self.assertEqual('0,0,NORTH', res)


if __name__ == '__main__':
    unittest.main()
