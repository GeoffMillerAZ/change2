# Author Geoff Miller
# Date: 12-26-15
# Currency Problem

from Errors import ErrorCodes
from Errors import ErrorMessages
from Currency import Currency
from Switch import Switch
import sys


class Prompt:
    """
    Handles the user input prompt
    """
    yes_no_str = "(y/n)"
    yeses = ["y","yes"]
    nos = ["n","no"]
    aborts = ["a", "exit", "abort", "stop", "esc"]


    @classmethod
    def begin(cls):
        """

        :return:
        """
        cls.print_header()
        if not cls.input_args():
            cls.input_currency()
        cls.print_footer()

    @classmethod
    def print_header(cls):
        """

        :return:
        """
        print("*******************************************")
        print("Welcome to my coin combinator!")
        print("*******************************************")

    @classmethod
    def print_footer(cls):
        """

        :return:
        """
        print("*******************************************")
        print("Thank you for your input. Parameters are:")
        print("*******************************************")
        print("Now printing combinations:")

    @classmethod
    def input_currency(cls):
        """

        :return:
        """
        is_input_complete = False
        is_valid_input = False
        while not is_input_complete:
            print("Let's define a coin. We need a name and a value.")
            while not is_valid_input:
                is_valid_input = False
                print("What is this new coin's name: ")
                input_currency_name = input("Name: ")
                if input_currency_name.isalpha():
                    is_valid_input = True
            is_valid_input = False
            while not is_valid_input:
                is_valid_input = False
                print("how many %s coins will it take to reach the target value? ")
                input_currency_value = input("Amount: ")
                if not input_currency_name.isalpha():
                    is_valid_input = True
            is_valid_input = False
            while not is_valid_input:
                is_valid_input = False
                input_define_another = input("Would you like to define another? %s", cls.yes_no_str)
                if input_define_another in cls.yeses:
                    is_input_complete = False
                elif input_define_another in cls.nos:
                    is_input_complete = True
                else:
                    print("Unrecognized input: please try again")
                    print()

    @classmethod
    def input_args(cls):
        """

        :return:
        """
        is_valid_input = False
        while not is_valid_input:
            input_default_currency = input("%s %s" % ("Would you like to use the default currency? ", cls.yes_no_str))
            if str.lower(input_default_currency) in cls.yeses:
                Params.is_streamlined = True
                Params.use_default_currency()
                is_valid_input = True
            elif str.lower(input_default_currency) in cls.nos:
                Params.is_streamlined = False
                is_valid_input = True
                break
            elif str.lower(input_default_currency) in cls.aborts:
                Params.user_exit()
                is_valid_input = True
                break
            else:
                print("Unrecognized input. Please try again: ")
        return Params.is_streamlined



class Params:
    """

    """
    is_streamlined = False
    target = None

    @classmethod
    def use_default_currency(cls):
        # cls.target = 100
        # Currency.define("quarter", 25)
        # Currency.define("dime", 10)
        # Currency.define("nickle", 5)
        # Currency.define("penny", 1)
        # Currency.process_defined_values()

        cls.target = 1500
        Currency.define("coin", 1000)
        Currency.define("arrowhead", 500)
        Currency.define("button", 10)
        Currency.process_defined_values()

    @classmethod
    def user_exit(cls):
        """
        Used for users choice to abort execution
        :return:
        """
        cls.exit_program(ErrorCodes.E_USER_EXIT)


    @classmethod
    def error_exit(cls, error_code):
        """
        Useed when aborting in error
        :param error_code: error code to return to calling program
        :return:
        """
        cls.exit_program(error_code)

    @classmethod
    def exit_program(cls, return_code):
        """
        Helper method for standardizing exit routines
        :param return_code: return code
        :return:
        """
        print("Exiting due to: %s" % (ErrorMessages.verbose(return_code)))
        sys.exit(return_code)


class Combinator:
    """
    Handles the Calculation and Output of the results set
    """
    # place to store solutions
    solutions = []

    @classmethod
    def calc(cls, remain, cointh, solution, add):
        # print("remain: %s\ncointh: %s = %s\nsolution: %s" % (remain, cointh, Currency.sorted_val(cointh), solution))
        """
        This method uses recursion to solve the problem. It works down
        the list of coins and starts with the biggest.
        # :param add: part to add to the solution workspace
        :param solution: scratch space for solution being assembled
        :param cointh: nth position of this coin in the sorted list
        :param remain: remaining value to solve for after coins put toward solution
        :return: a recursive call to self
        """
        if cointh == len(Currency.r_values):
            return 0
        if add:
            solution.append(add)
        if remain < 0:
            return 0
        if remain == 0:
            while cointh < len(Currency.r_values):
                solution.append((0, Currency.get_coin_name(Currency.sorted_val(cointh))))
                cointh += 1
            print(solution)
            Currency.num_solutions += 1
            return 1
        if (cointh + 1) == len(Currency.r_values):
            if remain % Currency.sorted_val(cointh) == 0:
                solution.append((int(remain / Currency.sorted_val(cointh)), Currency.get_coin_name(Currency.sorted_val(cointh))))
                print(solution)
                Currency.num_solutions += 1
                return 1
            else:
                return 0
        for x in range(0, int(remain/Currency.sorted_val(cointh)) + 1):
            cls.calc(remain - (x * (Currency.sorted_val(cointh))), cointh + 1, solution[:],
                     (x, Currency.get_coin_name(Currency.sorted_val(cointh))))
        return

    @classmethod
    def print(cls):
        """

        :return:
        """

def main():
    """
    Glossary:
    ** "Coin" may be used to refer to a currency unit

    :return: See ErrorCodes Class for return codes
    """
    # prompt
    Prompt.begin()

    # Process combinations
    Combinator.calc(Params.target, 0, [], None)
    print("DONE")
    print(Currency.num_solutions)
    print("xxx")
    print(len(Currency.solutions))

    # Print results
    Combinator.print()

    return ErrorCodes.R_SUCCESS


if __name__ == "__main__":
    main()