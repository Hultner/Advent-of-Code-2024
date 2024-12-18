from typing import Iterator

def parse_num_matrix(raw_input: str) -> Iterator[tuple[int, ...]]:
    # Split lines and numbers
    data = (line.split() for line in raw_input.splitlines())
    # Create numbers
    numbers = (tuple(map(int, line)) for line in data)
    return numbers
