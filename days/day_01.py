from typing import List

from day_factory.day import Day
from day_factory.day_utils import TestEnum


class Day01(Day):
    FIRST_STAR_TEST_RESULT = 0
    SECOND_STAR_TEST_RESULT = 0

    def __init__(self):
        super().__init__(self)

    @staticmethod
    def count_id(input_value: List[str]) -> int:
        return 0

    @staticmethod
    def count_id_2(input_value: List[str]) -> int:
        return 0

    def solution_first_star(self, input_value: List[str], input_type: TestEnum) -> int:
        return self.count_id(input_value)

    def solution_second_star(self, input_value: List[str], input_type: TestEnum) -> int:
        return self.count_id_2(input_value)
