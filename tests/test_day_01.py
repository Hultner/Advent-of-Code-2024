from typing import Any

from aoc.day_01.core import part_1, part_2

sample_seed_1 = """3   4
4   3
2   5
1   3
3   9
3   3"""

answers = (
    2086478,
    0,
)


def test_parts() -> None:
    # Oracle says so
    assert part_1(sample_seed_1) == 11
    assert part_1() == answers[0]
    assert part_2(sample_seed_1) == 31
    assert part_2() == 0


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
