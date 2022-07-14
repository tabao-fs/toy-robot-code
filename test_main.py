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


if __name__ == '__main__':
    unittest.main()
