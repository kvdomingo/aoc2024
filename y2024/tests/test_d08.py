from y2024.d08.core import load_input, part1, part2


def test_part1():
    data = load_input(is_test=True)
    assert part1(data) == 14


def test_part2():
    data = load_input(is_test=True)
    assert part2(data) == 34
