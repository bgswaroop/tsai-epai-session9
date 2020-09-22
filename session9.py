from functools import singledispatch
from html import escape
from numbers import Integral, Real
from decimal import Decimal


def allow_odd_seconds_decorator(func):
    """
    A decorator which executes the function only when called at an odd second!
    :param func: Any function
    :return: the inner function
    """
    from datetime import datetime
    from functools import wraps

    @wraps(func)
    def inner(*args, **kwargs):
        """
        Inner method for allow_odd_seconds_decorator
        :param args: positional arguments
        :param kwargs: keyword arguments
        :return: func(...)
        """
        now = datetime.now()
        current_seconds = int(now.strftime("%S"))
        print('seconds from decorator', current_seconds)

        if current_seconds % 2 == 1:
            print(f'Running the function {func.__name__}')
            return func(*args, **kwargs)
        else:
            print(f'You are unlucky, try re-running at an odd second :)')
            return None

    return inner


def log_decorator(fn):
    """
    Decorator to add some logs when a method is called
    :param fn: Any function
    :return: the inner function
    """
    from functools import wraps
    from datetime import datetime, timezone

    @wraps(fn)
    def inner(*args, **kwargs):
        """
        Inner method for log_decorator
        :param args: positional arguments
        :param kwargs: keyword arguments
        :return: func(...)
        """
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print(f'{run_dt}: called {fn.__name__}')
        print(f'Description: {fn.__doc__}')
        print(f'Arguments: {args} {kwargs}')
        return result

    return inner


def set_password(password):
    """
    A method to set a password
    :return: the inner function
    """

    def inner():
        """
        The inner function for set_password
        :return: password
        """
        nonlocal password
        return password

    return inner


def authenticate_decorator_factory(current_password, user_password):
    """
    Authenticate the user with the current_password
    :param current_password: an instance of decorator set_password
    :param user_password: user provided password
    :return: decorator
    """

    def authenticate_decorator(fn):
        """
        Decorator method for the factory authenticate_decorator_factory
        :param fn: any function
        :return: the function if the user password is correct
        """
        cnt = 0
        from functools import wraps

        if user_password == current_password():
            @wraps(fn)
            def inner(*args, **kwargs):
                """
                Inner method for authenticate_decorator
                :param args: positional arguments
                :param kwargs: keyword arguments
                :return: function
                """
                nonlocal cnt
                cnt += 1
                print(f'{fn.__name__} was called {cnt} times')
                return fn(*args, **kwargs)

            return inner
        else:
            print('You scammer!!')
            return lambda *args, **kwargs: None

    return authenticate_decorator


def timed(num_iterations):
    """
    A decorator factory
    :param num_iterations:
    :return: decorator
    """

    def timed_decorator(fn):
        """
        A decorator
        :param fn: any function
        :return: inner
        """
        nonlocal num_iterations
        from time import perf_counter

        def inner(*args, **kwargs):
            """
            the inner method for the timed_decorator
            :param args:
            :param kwargs:
            :return:
            """

            nonlocal num_iterations
            start = perf_counter()
            for _ in range(num_iterations):
                fn(*args, **kwargs)
            end = perf_counter()

            execution_time = (end - start) / num_iterations
            print(f'\nThe function {fn.__name__} takes on an average {execution_time} sec')
            return fn(*args, **kwargs)

        return inner

    return timed_decorator


def control_access(access_level):
    """
    Decorator factory
    :param access_level: an integer [1, 2, 3, 4] determining the access for a user
    :return: access_decorator
    """

    def access_decorator(fn):
        """
        A decorator for the factory control_access
        :param fn: any function that supports additional positional arguments
        :return: inner function
        """
        nonlocal access_level
        a = 1  # available to access level 1 and above
        b = 2  # available to access level 2 and above
        c = 3  # available to access level 3 and above
        d = 4  # available to access level 4

        access_elements = {1: (a,), 2: (a, b), 3: (a, b, c), 4: (a, b, c, d)}

        def inner(*args, **kwargs):
            """
            the inner method corresponding to access_decorator
            :param args: positional arguments
            :param kwargs: keyword arguments
            :return: function
            """
            nonlocal access_level

            additional_arguments = access_elements.get(access_level, ())
            return fn(*args, *additional_arguments, **kwargs)

        return inner

    return access_decorator


@singledispatch
def htmlize(a):
    """
    htmlize generic function
    :param a: generic type
    :return: htmlized string
    """
    return escape(str(a))


@htmlize.register(Integral)
def htmlize_integral_numbers(a):
    """
    :param a: Integral number
    :return: htmlized string
    """
    return f'{a}(<i>{str(hex(a))}</i>)'


@htmlize.register(Real)
def html_real(a):
    """
    :param a: Real number
    :return: htmlized string
    """
    return f'{round(a, 2)}'


@htmlize.register(Decimal)
def html_real(a):
    """
    :param a: Decimal number
    :return: htmlized string
    """
    return f'{round(a, 2)}'


@htmlize.register(str)
def html_str(s):
    """
    :param s: string
    :return: htmlized string
    """
    return escape(str(s)).replace('\n', '<br/>\n')


@htmlize.register(tuple)
@htmlize.register(list)
def html_list(l):
    """
    :param l: tuple, string
    :return: htmlized string
    """
    items = (f'<li>{escape(str((item)))}</li>' for item in l)
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


@htmlize.register(dict)
def html_dict(d):
    """
    :param d: dictionary
    :return: htmlized string
    """
    items = (f'<li>{k}={v}</li>' for k, v in d.items())
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


@htmlize.register(set)
def html_set(arg):
    """
    :param arg: set
    :return: htmlized string
    """
    return html_list(arg)
