from problems.number_of_students_unable_to_eat.solution_counter import count_students as _count_students_counter
from problems.number_of_students_unable_to_eat.solution_queue import count_students as _count_students_queue
from test_utils.base_in_out_test import BaseInOutTestCase


def count_students_counter(students, sandwiches):
    """Counter-based solution"""
    return _count_students_counter(students, sandwiches)


def count_students_queue(students, sandwiches):
    """Queue-based solution"""
    return _count_students_queue(students, sandwiches)


class TestCountStudents(BaseInOutTestCase):
    function_under_test = [count_students_counter, count_students_queue]

    test_cases = [
        ("basic case", ([1, 1, 0, 0], [0, 1, 0, 1]), 0),
        ("some students unable to eat", ([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]), 3),
        ("all students eat", ([0, 0, 0], [0, 0, 0]), 0),
        ("all students unable to eat circle", ([1, 1, 1], [0, 0, 0]), 3),
        ("all students unable to eat square", ([0, 0, 0], [1, 1, 1]), 3),
        ("single student gets food", ([1], [1]), 0),
        ("single student no food", ([0], [1]), 1),
        ("alternating pattern all served", ([0, 1, 0, 1], [0, 1, 0, 1]), 0),
        ("mixed preferences some left", ([1, 0, 1, 0], [1, 1, 0, 0]), 0),
        ("circle students first", ([0, 0, 1, 1], [0, 0, 1, 1]), 0),
        ("square students first", ([1, 1, 0, 0], [1, 1, 0, 0]), 0),
        ("no circle students", ([1, 1, 1], [1, 1, 1]), 0),
        ("no square students", ([0, 0, 0], [0, 0, 0]), 0),
        ("complex case with blocking", ([1, 0, 0, 1, 0, 1, 1], [0, 0, 0, 1, 1, 1, 1]), 0),
        ("edge case single type", ([1, 1], [0, 0]), 2),
        ("reverse order", ([0, 1], [1, 0]), 0),
        ("large case all different", ([0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0]), 0),
        ("unbalanced preferences", ([1, 1, 1, 0], [0, 0, 1, 1]), 3),
        ("early blocking", ([0, 1, 1], [1, 1, 1]), 1),
        ("late availability", ([1, 1, 0], [1, 1, 0]), 0),
    ]


if __name__ == "__main__":
    import unittest

    unittest.main()