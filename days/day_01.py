from day_factory.day import Day
from day_factory.day_utils import TestEnum
from utils.input_parser import InputParser


class Day01(Day):
    FIRST_STAR_TEST_RESULT = 3
    SECOND_STAR_TEST_RESULT = 1

    def __init__(self):
        super().__init__(self)

    @staticmethod
    def count_id(input_value: InputParser) -> int:
        return sum(
            map(lambda x: 1 if x == "(" else -1, next(input_value.get_iterator()))
        )

    @staticmethod
    def count_id_2(input_value: InputParser) -> int:
        instructions = next(input_value.get_iterator())
        floor = 0
        for i, c in enumerate(instructions):
            floor += 1 if c == "(" else -1
            if floor == -1:
                return i + 1

    def solution_first_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.count_id(input_value)

    def solution_second_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.count_id_2(input_value)
