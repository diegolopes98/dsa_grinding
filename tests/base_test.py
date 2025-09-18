import unittest
from typing import Any, List, Tuple, Callable


class ParameterizedTestCase(unittest.TestCase):
    """
    Abstract base class for creating parameterized tests.

    Usage:
    1. Inherit from this class
    2. Set the function_under_test class attribute to your function
    3. Set the test_cases class attribute to a list of tuples containing:
       (test_name, input_args, expected_output)
    """

    function_under_test: Callable = None
    test_cases: List[Tuple[str, Tuple, Any]] = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        if cls.__name__ in ["ParameterizedTestCaseWithSetup"]:
            return

        if cls.function_under_test is None:
            raise ValueError(f"{cls.__name__} must define function_under_test")

        if not cls.test_cases:
            raise ValueError(f"{cls.__name__} must define test_cases")

        for test_name, input_args, expected_output in cls.test_cases:
            cls._create_test_method(test_name, input_args, expected_output)

    @classmethod
    def _create_test_method(
        cls, test_name: str, input_args: Tuple, expected_output: Any
    ):
        """Create a test method dynamically"""

        def test_method(self):
            result = cls.function_under_test(*input_args)
            self.assertEqual(
                result,
                expected_output,
                f"Failed for test '{test_name}' with inputs {input_args}",
            )

        method_name = f"test_{test_name.lower().replace(' ', '_').replace('-', '_')}"
        test_method.__name__ = method_name
        test_method.__doc__ = f"Test case: {test_name}"

        setattr(cls, method_name, test_method)


class ParameterizedTestCaseWithSetup(ParameterizedTestCase):
    """
    Extended version that allows custom setup and teardown for each test case.

    Usage:
    Same as ParameterizedTestCase, but you can optionally override:
    - setup_test_case(test_name, input_args) - called before each test
    - teardown_test_case(test_name, input_args) - called after each test
    """

    def setup_test_case(self, test_name: str, input_args: Tuple):
        """Override this method to add custom setup for each test case"""
        pass

    def teardown_test_case(self, test_name: str, input_args: Tuple):
        """Override this method to add custom teardown for each test case"""
        pass

    @classmethod
    def _create_test_method(
        cls, test_name: str, input_args: Tuple, expected_output: Any
    ):
        """Create a test method with setup/teardown support"""

        def test_method(self):
            self.setup_test_case(test_name, input_args)
            try:
                result = cls.function_under_test(*input_args)
                self.assertEqual(
                    result,
                    expected_output,
                    f"Failed for test '{test_name}' with inputs {input_args}",
                )
            finally:
                self.teardown_test_case(test_name, input_args)

        method_name = f"test_{test_name.lower().replace(' ', '_').replace('-', '_')}"
        test_method.__name__ = method_name
        test_method.__doc__ = f"Test case: {test_name}"

        setattr(cls, method_name, test_method)
