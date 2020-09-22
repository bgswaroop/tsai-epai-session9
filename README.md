# EPAi session9 assignment
---

The following requirements need to be met to successfully run the code : 
Dependencies  :   python > = 3.7.4 \
Python packages  :   refer to requirements.txt

---
## Session9 objectives
This assignment, helps to code the concepts that are learnt in the session 8 of the EPAi module. 
In particular, this assignment focuses on the following topics  : 

 - Decorators
 - Parameterized Decorators
 
---

The test cases can be executed by executing _pytest_, from python shell
 
---

### Functions


**allow_odd_seconds_decorator(func)**

    A decorator which executes the function only when called at an odd second!
     : param func :  Any function
     : return :  the inner function

**inner(\*args, \*\*kwargs)**

        Inner method for allow_odd_seconds_decorator
         : param args :  positional arguments
         : param kwargs :  keyword arguments
         : return :  func(...)

**log_decorator(fn)**

    Decorator to add some logs when a method is called
     : param fn :  Any function
     : return :  the inner function

**inner(\*args, \*\*kwargs)**

        Inner method for log_decorator
         : param args :  positional arguments
         : param kwargs :  keyword arguments
         : return :  func(...)

**set_password(password)**

    A method to set a password
     : return :  the inner function

**inner()**

        The inner function for set_password
         : return :  password

**authenticate_decorator_factory(current_password, user_password)**

    Authenticate the user with the current_password
     : param current_password :  an instance of decorator set_password
     : param user_password :  user provided password
     : return :  decorator

**authenticate_decorator(fn)**

        Decorator method for the factory authenticate_decorator_factory
         : param fn :  any function
         : return :  the function if the user password is correct

**inner(\*args, \*\*kwargs)**

                Inner method for authenticate_decorator
                 : param args :  positional arguments
                 : param kwargs :  keyword arguments
                 : return :  function

**timed(num_iterations)**

    A decorator factory
     : param num_iterations : 
     : return :  decorator

**timed_decorator(fn)**

        A decorator
         : param fn :  any function
         : return :  inner

**inner(\*args, \*\*kwargs)**

            the inner method for the timed_decorator
             : param args : 
             : param kwargs : 
             : return : 

**control_access(access_level)**

    Decorator factory
     : param access_level :  an integer [1, 2, 3, 4] determining the access for a user
     : return :  access_decorator

**access_decorator(fn)**

        A decorator for the factory control_access
         : param fn :  any function that supports additional positional arguments
         : return :  inner function

**inner(\*args, \*\*kwargs)**

            the inner method corresponding to access_decorator
             : param args :  positional arguments
             : param kwargs :  keyword arguments
             : return :  function

**htmlize(a)**

    htmlize generic function
     : param a :  generic type
     : return :  htmlized string

**htmlize_integral_numbers(a)**

     : param a :  Integral number
     : return :  htmlized string

**html_real(a)**

     : param a :  Real number
     : return :  htmlized string

**html_real(a)**

     : param a :  Decimal number
     : return :  htmlized string

**html_str(s)**

     : param s :  string
     : return :  htmlized string

**html_list(l)**

     : param l :  tuple, string
     : return :  htmlized string

**html_dict(d)**

     : param d :  dictionary
     : return :  htmlized string

**html_set(arg)**

     : param arg :  set
     : return :  htmlized string

---

### Unit Tests


**test_readme_exists()**

    Check if the README file exists
     : return :  None

**test_readme_contents()**

    Test the length of the README file
     : return :  None

**test_readme_file_for_formatting()**

    Tests the formatting for the README file
     : return :  None

**test_function_name_had_cap_letter()**

    Checking PEP-8 guidelines for function names. Pass if all alphabets(a-z) are in small case.
     : return :  None

**test_allow_odd_seconds_decorator()**

    Test the generator allow_odd_seconds_decorator
     : return :  None

**my_add(x, y)**


**test_log_decorator1()**

    test the log_decorator
     : return :  None

**my_add(a, b)**

        This method adds two elements a and b, when the binary + operator is defined for its elements
         : param a :  an object of type T
         : param b :  an object of type T
         : return :  sum

**test_log_decorator2()**

    test the log_decorator
     : return :  None

**my_square(a)**

        Square a number
         : param a :  any valid number
         : return :  Square of the number

**test_authenticate_decorator1()**

    test the method authenticate_decorator
     : return :  None

**my_add(a, b)**

        This method adds two elements a and b, when the binary + operator is defined for its elements
         : param a :  an object of type T
         : param b :  an object of type T
         : return :  sum

**test_authenticate_decorator2()**

    test the method authenticate_decorator
     : return :  None

**my_sub(a, b)**

        This method adds two elements a and b, when the binary + operator is defined for its elements
         : param a :  an object of type T
         : param b :  an object of type T
         : return :  subtraction

**test_timed1()**

    test the decorator factory timed
     : return :  None

**my_add(a, b)**

        This method adds two elements a and b, when the binary + operator is defined for its elements
         : param a :  an object of type T
         : param b :  an object of type T
         : return :  sum

**test_timed2()**

    test the decorator factory timed
     : return :  None

**my_square(a)**

        Square a number
         : param a :  any valid number
         : return :  Square of the number

**test_control_access1()**

    test the control access factory with access level 1
     : return :  None

**add(\*args)**

        Add all the arguments
         : param args :  positional arguments, all numbers of same type
         : return :  sum

**test_control_access2()**

    test the control access factory with access level 2
     : return :  None

**add(\*args)**

        Add all the arguments
         : param args :  positional arguments, all numbers of same type
         : return :  sum

**test_control_access3()**

    test the control access factory with access level 3
     : return :  None

**add(\*args)**

        Add all the arguments
         : param args :  positional arguments, all numbers of same type
         : return :  sum

**test_control_access4()**

    test the control access factory with access level 4
     : return :  None

**add(\*args)**

        Add all the arguments
         : param args :  positional arguments, all numbers of same type
         : return :  sum

**test_control_access5()**

    test the control access factory with access level None
     : return :  None

**add(\*args)**

        Add all the arguments
         : param args :  positional arguments, all numbers of same type
         : return :  sum

**test_htmlized1()**

    test the htmlized strings
     : return :  None

**test_htmlized2()**

    test the htmlized integers
     : return :  None

**test_htmlized3()**

    test the htmlized real numbers
     : return :  None

**test_htmlized4()**

    test the htmlized decimal numbers
     : return :  None

**test_htmlized5()**

    test the htmlized tuples
     : return :  None

**test_htmlized6()**

    test the htmlized lists
     : return :  None

**test_htmlized7()**

    test the htmlized dictionaries
     : return :  None

**test_htmlized8()**

    test the htmlized set
     : return :  None

---

#### 