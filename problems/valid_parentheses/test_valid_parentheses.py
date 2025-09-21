from problems.valid_parentheses.solution import is_valid
from test_utils.base_in_out_test import BaseInOutTestCase


class TestIsValid(BaseInOutTestCase):
    function_under_test = is_valid

    test_cases = [
        ("valid basic parentheses", ("()",), True),
        ("valid multiple types", ("()[]{}",), True),
        ("valid nested", ("([{}])",), True),
        ("valid complex nested", ("{[()]}",), True),
        ("valid multiple pairs", ("()()",), True),
        ("valid mixed order", ("({[]})",), True),
        ("valid deep nesting", ("((()))",), True),
        ("valid all types nested", ("[({})]",), True),
        ("invalid mismatched", ("(]",), False),
        ("invalid wrong order", ("([)]",), False),
        ("invalid extra closing", ("())",), False),
        ("invalid extra opening", ("(()",), False),
        ("invalid single opening", ("(",), False),
        ("invalid single closing", (")",), False),
        ("invalid mixed mismatch", ("([{})]",), False),
        ("invalid only closing", ("]]]",), False),
        ("invalid only opening", ("[[[",), False),
        ("invalid interleaved", ("([)]",), False),
        ("empty string", ("",), True),
        ("single pair brackets", ("[]",), True),
        ("single pair braces", ("{}",), True),
        ("invalid bracket paren mismatch", ("(]",), False),
        ("invalid brace bracket mismatch", ("{]",), False),
        ("invalid brace paren mismatch", ("{)",), False),
        ("valid long sequence", ("()[]{}()[]{}",), True),
        ("invalid unbalanced complex", ("((()",), False),
        ("invalid reverse order", ("}{",), False),
        ("valid alternating types", ("({})[]",), True),
        ("invalid crossing pairs", ("([])()}{",), False),
        ("large valid sequence", ("(((((((((()))))))))))",), True),
        ("large invalid sequence", ("(((((((((())))))))",), False),
    ]


if __name__ == "__main__":
    import unittest

    unittest.main()