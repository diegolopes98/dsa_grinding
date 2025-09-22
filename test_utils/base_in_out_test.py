import unittest
from typing import Any, List, Tuple, Callable


class BaseInOutTestCase(unittest.TestCase):
    """
    Abstract base class for creating input-output tests.

    Usage:
    1. Inherit from this class
    2. Set the function_under_test class attribute to a list of functions
    3. Set the test_cases class attribute to a list of tuples containing:
       (test_name, input_args, expected_output)
    """

    function_under_test: List[Callable] = []
    test_cases: List[Tuple[str, Tuple, Any]] = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        if cls.__name__ in ["BaseInOutTestCaseWithSetup"]:
            return

        if not cls.function_under_test:
            raise ValueError(f"{cls.__name__} must define function_under_test as a list of functions")

        if not cls.test_cases:
            raise ValueError(f"{cls.__name__} must define test_cases")

        for test_name, input_args, expected_output in cls.test_cases:
            for i, func in enumerate(cls.function_under_test):
                func_name = getattr(func, '__name__', f'function_{i}')
                if len(cls.function_under_test) > 1:
                    # Multiple functions: create separate test for each
                    test_method_name = f"{test_name}_{func_name}"
                else:
                    # Single function: use original test name
                    test_method_name = test_name

                cls._create_test_method(test_method_name, input_args, expected_output, func, func_name)

    @classmethod
    def _create_test_method(
        cls, test_name: str, input_args: Tuple, expected_output: Any, func: Callable, func_name: str
    ):
        """Create a test method dynamically"""

        def test_method(self):
            result = func(*input_args)
            self.assertEqual(
                result,
                expected_output,
                f"Failed for test '{test_name}' using function '{func_name}' with inputs {input_args}",
            )

        method_name = f"test_{test_name.lower().replace(' ', '_').replace('-', '_')}"
        test_method.__name__ = method_name
        test_method.__doc__ = f"Test case: {test_name} (using {func_name})"

        setattr(cls, method_name, test_method)


class BaseInOutTestCaseWithSetup(BaseInOutTestCase):
    """
    Extended version that allows custom setup and teardown for each test case.

    Usage:
    Same as BaseInOutTestCase, but you can optionally override:
    - setup_test_case(test_name, input_args, func_name) - called before each test
    - teardown_test_case(test_name, input_args, func_name) - called after each test
    """

    def setup_test_case(self, test_name: str, input_args: Tuple, func_name: str):
        """Override this method to add custom setup for each test case"""
        pass

    def teardown_test_case(self, test_name: str, input_args: Tuple, func_name: str):
        """Override this method to add custom teardown for each test case"""
        pass

    @classmethod
    def _create_test_method(
        cls, test_name: str, input_args: Tuple, expected_output: Any, func: Callable, func_name: str
    ):
        """Create a test method with setup/teardown support"""

        def test_method(self):
            self.setup_test_case(test_name, input_args, func_name)
            try:
                result = func(*input_args)
                self.assertEqual(
                    result,
                    expected_output,
                    f"Failed for test '{test_name}' using function '{func_name}' with inputs {input_args}",
                )
            finally:
                self.teardown_test_case(test_name, input_args, func_name)

        method_name = f"test_{test_name.lower().replace(' ', '_').replace('-', '_')}"
        test_method.__name__ = method_name
        test_method.__doc__ = f"Test case: {test_name} (using {func_name})"

        setattr(cls, method_name, test_method)
