from day_factory.day import Day
from day_factory.day_utils import TestEnum
from utils.input_parser import InputParser


class Day03(Day):
    FIRST_STAR_TEST_RESULT = 2
    SECOND_STAR_TEST_RESULT = 11

    DIRECTION = {"^": -1, "v": 1, ">": 1j, "<": -1j}

    def __init__(self):
        super().__init__(self)

    @staticmethod
    def count_id(input_value: InputParser) -> int:
        houses = {0}
        pos = 0
        for c in next(input_value.get_iterator()):
            pos += Day03.DIRECTION[c]
            houses.add(pos)
        return len(houses)

    @staticmethod
    def count_id_2(input_value: InputParser) -> int:
        houses = {0}
        pos = 0
        robo_pos = 0
        for idx, c in enumerate(next(input_value.get_iterator())):
            if idx % 2 == 0:
                pos += Day03.DIRECTION[c]
                houses.add(pos)
            else:
                robo_pos += Day03.DIRECTION[c]
                houses.add(robo_pos)
        return len(houses)

    def solution_first_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.count_id(input_value)

    def solution_second_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.count_id_2(input_value)
