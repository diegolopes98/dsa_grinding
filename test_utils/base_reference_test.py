import unittest
from typing import Any, List, Tuple, Callable
import copy


class BaseReferenceTestCase(unittest.TestCase):
    """
    Abstract base class for creating tests that modify inputs in-place.

    Usage:
    1. Inherit from this class
    2. Set the function_under_test class attribute to your function
    3. Set the test_cases class attribute to a list of tuples containing:
       (test_name, input_args, assertion_function)

    The assertion_function should take the modified input_args and perform
    custom assertions on them.

    Example:
        def test_reverse_array(original_input, modified_input):
            nums = modified_input[0]  # First argument
            assert nums == [3, 2, 1], f"Expected [3, 2, 1], got {nums}"

        test_cases = [
            ("reverse simple array", ([1, 2, 3],), test_reverse_array),
        ]
    """

    function_under_test: Callable = None
    test_cases: List[Tuple[str, Tuple, Callable]] = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        if cls.__name__ in ["BaseReferenceTestCaseWithSetup"]:
            return

        if cls.function_under_test is None:
            raise ValueError(f"{cls.__name__} must define function_under_test")

        if not cls.test_cases:
            raise ValueError(f"{cls.__name__} must define test_cases")

        for test_name, input_args, assertion_func in cls.test_cases:
            cls._create_test_method(test_name, input_args, assertion_func)

    @classmethod
    def _create_test_method(
        cls, test_name: str, input_args: Tuple, assertion_func: Callable
    ):
        """Create a test method dynamically"""

        def test_method(self):
            # Deep copy the input to preserve original for assertion
            original_input = copy.deepcopy(input_args)
            modified_input = copy.deepcopy(input_args)

            # Call the function with the modified input
            cls.function_under_test(*modified_input)

            # Run the custom assertion
            try:
                assertion_func(original_input, modified_input)
            except Exception as e:
                self.fail(
                    f"Failed for test '{test_name}' with inputs {original_input}: {str(e)}"
                )

        method_name = f"test_{test_name.lower().replace(' ', '_').replace('-', '_')}"
        test_method.__name__ = method_name
        test_method.__doc__ = f"Test case: {test_name}"

        setattr(cls, method_name, test_method)


class BaseReferenceTestCaseWithSetup(BaseReferenceTestCase):
    """
    Extended version that allows custom setup and teardown for each test case.

    Usage:
    Same as BaseReferenceTestCase, but you can optionally override:
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
        cls, test_name: str, input_args: Tuple, assertion_func: Callable
    ):
        """Create a test method with setup/teardown support"""

        def test_method(self):
            self.setup_test_case(test_name, input_args)
            try:
                # Deep copy the input to preserve original for assertion
                original_input = copy.deepcopy(input_args)
                modified_input = copy.deepcopy(input_args)

                # Call the function with the modified input
                cls.function_under_test(*modified_input)

                # Run the custom assertion
                try:
                    assertion_func(original_input, modified_input)
                except Exception as e:
                    self.fail(
                        f"Failed for test '{test_name}' with inputs {original_input}: {str(e)}"
                    )
            finally:
                self.teardown_test_case(test_name, input_args)

        method_name = f"test_{test_name.lower().replace(' ', '_').replace('-', '_')}"
        test_method.__name__ = method_name
        test_method.__doc__ = f"Test case: {test_name}"

        setattr(cls, method_name, test_method)