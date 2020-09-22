import inspect
import os
import re

import session9
from session9 import *


def test_readme_exists():
    """
    Check if the README file exists
    :return: None
    """
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    """
    Test the length of the README file
    :return: None
    """
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add at least 500 words"


def test_readme_file_for_formatting():
    """
    Tests the formatting for the README file
    :return: None
    """
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_function_name_had_cap_letter():
    """
    Checking PEP-8 guidelines for function names. Pass if all alphabets(a-z) are in small case.
    :return: None
    """
    functions = inspect.getmembers(session9, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_allow_odd_seconds_decorator():
    """
    Test the generator allow_odd_seconds_decorator
    :return: None
    """

    @allow_odd_seconds_decorator
    def my_add(x, y):
        return x + y

    import time, random

    for _ in range(20):
        time.sleep(random.random())
        result = my_add(1, 2)
        if result:
            assert result == 3


def test_log_decorator1():
    """
    test the log_decorator
    :return: None
    """

    @log_decorator
    def my_add(a, b):
        """
        This method adds two elements a and b, when the binary + operator is defined for its elements
        :param a: an object of type T
        :param b: an object of type T
        :return: sum
        """
        return a + b

    result = my_add(1, 2)
    assert result == 3


def test_log_decorator2():
    """
    test the log_decorator
    :return: None
    """

    @log_decorator
    def my_square(a):
        """
        Square a number
        :param a: any valid number
        :return: Square of the number
        """
        return a ** 2

    result = my_square(0)
    assert result == 0


def test_authenticate_decorator1():
    """
    test the method authenticate_decorator
    :return: None
    """

    current_password = set_password('sai_ram')
    user_password = 'sai_ram'

    @authenticate_decorator_factory(current_password, user_password)
    def my_add(a, b):
        """
        This method adds two elements a and b, when the binary + operator is defined for its elements
        :param a: an object of type T
        :param b: an object of type T
        :return: sum
        """
        return a + b

    result = my_add(1, 2)
    assert result == 3
    result = my_add(-1, 2)
    assert result == 1


def test_authenticate_decorator2():
    """
    test the method authenticate_decorator
    :return: None
    """
    current_password = set_password('sai_ram')
    user_password = 'scam'

    @authenticate_decorator_factory(current_password, user_password)
    def my_sub(a, b):
        """
        This method adds two elements a and b, when the binary + operator is defined for its elements
        :param a: an object of type T
        :param b: an object of type T
        :return: subtraction
        """
        return a - b

    result = my_sub(1, 2)
    assert result is None


def test_timed1():
    """
    test the decorator factory timed
    :return: None
    """

    @timed(100)
    def my_add(a, b):
        """
        This method adds two elements a and b, when the binary + operator is defined for its elements
        :param a: an object of type T
        :param b: an object of type T
        :return: sum
        """
        return a + b

    result = my_add(1, 2)
    assert result == 3


def test_timed2():
    """
    test the decorator factory timed
    :return: None
    """

    @timed(100)
    def my_square(a):
        """
        Square a number
        :param a: any valid number
        :return: Square of the number
        """
        return a ** 2

    result = my_square(500)
    assert result == 250000


def test_control_access1():
    """
    test the control access factory with access level 1
    :return: None
    """

    @control_access(access_level=1)
    def add(*args):
        """
        Add all the arguments
        :param args: positional arguments, all numbers of same type
        :return: sum
        """
        sum_args = 0
        for x in args:
            sum_args += x
        return sum_args

    result = add(1, 2)
    assert result == 4


def test_control_access2():
    """
    test the control access factory with access level 2
    :return: None
    """

    @control_access(access_level=2)
    def add(*args):
        """
        Add all the arguments
        :param args: positional arguments, all numbers of same type
        :return: sum
        """
        sum_args = 0
        for x in args:
            sum_args += x
        return sum_args

    result = add(1, 2)
    assert result == 6


def test_control_access3():
    """
    test the control access factory with access level 3
    :return: None
    """

    @control_access(access_level=3)
    def add(*args):
        """
        Add all the arguments
        :param args: positional arguments, all numbers of same type
        :return: sum
        """
        sum_args = 0
        for x in args:
            sum_args += x
        return sum_args

    result = add(1, 2)
    assert result == 9


def test_control_access4():
    """
    test the control access factory with access level 4
    :return: None
    """

    @control_access(access_level=4)
    def add(*args):
        """
        Add all the arguments
        :param args: positional arguments, all numbers of same type
        :return: sum
        """
        sum_args = 0
        for x in args:
            sum_args += x
        return sum_args

    result = add(1, 2)
    assert result == 13


def test_control_access5():
    """
    test the control access factory with access level None
    :return: None
    """

    @control_access(access_level=None)
    def add(*args):
        """
        Add all the arguments
        :param args: positional arguments, all numbers of same type
        :return: sum
        """
        sum_args = 0
        for x in args:
            sum_args += x
        return sum_args

    result = add(1, 2)
    assert result == 3


def test_htmlized1():
    """
    test the htmlized strings
    :return: None
    """

    result = htmlize('sai ram \n aum shanti')
    assert result == r"""sai ram <br/>
 aum shanti"""


def test_htmlized2():
    """
    test the htmlized integers
    :return: None
    """

    result = htmlize(123)
    assert result == r"""123(<i>0x7b</i>)"""


def test_htmlized3():
    """
    test the htmlized real numbers
    :return: None
    """

    result = htmlize(123.3445)
    assert result == '123.34'


def test_htmlized4():
    """
    test the htmlized decimal numbers
    :return: None
    """
    from decimal import Decimal
    result = htmlize(Decimal(32.2222222))
    assert result == '32.22'


def test_htmlized5():
    """
    test the htmlized tuples
    :return: None
    """

    result = htmlize((1, 2, 3, 4))
    assert result == r"""<ul>
<li>1</li>
<li>2</li>
<li>3</li>
<li>4</li>
</ul>"""


def test_htmlized6():
    """
    test the htmlized lists
    :return: None
    """

    result = htmlize([1, 2, 3, 4])
    assert result == r"""<ul>
<li>1</li>
<li>2</li>
<li>3</li>
<li>4</li>
</ul>"""


def test_htmlized7():
    """
    test the htmlized dictionaries
    :return: None
    """

    result = htmlize({1:2, 3:4})
    assert result == r"""<ul>
<li>1=2</li>
<li>3=4</li>
</ul>"""


def test_htmlized8():
    """
    test the htmlized set
    :return: None
    """

    result = htmlize({1, 2, 3, 4})
    assert result == r"""<ul>
<li>1</li>
<li>2</li>
<li>3</li>
<li>4</li>
</ul>"""

