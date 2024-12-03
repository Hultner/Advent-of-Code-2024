from typing import Any

from aoc.day_02.core import part_1, part_2

sample_seed_1 = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

answers = (
    2,
    4,
)


def test_parts() -> None:
    # Oracle says so
    assert part_1() == 516
    assert part_2() == 561


def verify_day(data: Any, expected_1: Any, expected_2: Any) -> None:
    assert part_1(data) == expected_1
    assert part_2(data) == expected_2


def test_samples() -> None:
    """
    Tests the given examples
    """
    examples = ((sample_seed_1, answers),)

    for data, expected in examples:
        verify_day(data, *expected)
