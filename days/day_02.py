import sys

from day_factory.day import Day
from day_factory.day_utils import TestEnum
from utils.input_parser import InputParser
from utils.utils import extract_int


class Day02(Day):
    FIRST_STAR_TEST_RESULT = 101
    SECOND_STAR_TEST_RESULT = 48

    def __init__(self):
        super().__init__(self)

    @staticmethod
    def count_id(input_value: InputParser) -> int:
        total = 0
        for box in input_value.get_iterator():
            dim = extract_int(box)
            slack = sys.maxsize
            for i in range(2):
                for j in range(i + 1, 3):
                    mul = dim[i] * dim[j]
                    total += 2 * mul
                    slack = min(slack, mul)
            total += slack
        return total

    @staticmethod
    def count_id_2(input_value: InputParser) -> int:
        total = 0
        for box in input_value.get_iterator():
            dim = extract_int(box)
            total += dim[0] * dim[1] * dim[2]
            total += 2 * (dim[0] + dim[1] + dim[2] - max(dim))
        return total

    def solution_first_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.count_id(input_value)

    def solution_second_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.count_id_2(input_value)
