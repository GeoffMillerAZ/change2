from Control import Control
from Currency import Currency


class Prompt:
    """
    Handles the user input prompt
    """
    yes_no_str = "(y/n)"
    yeses = ["y", "yes"]
    nos = ["n", "no"]
    aborts = ["a", "exit", "abort", "stop", "esc", "c", "cancel"]

    @classmethod
    def is_valid_control(cls, x):
        return True if x in cls.yeses or x in cls.nos or x in cls.aborts else False

    @classmethod
    def is_valid_alpha(cls, x):
        return True if str(x).isalpha() else False

    # noinspection PyUnusedLocal
    @classmethod
    def is_valid_numeric(cls, x):
        try:
            a = float(str(x))
        except ValueError:
            try:
                a = int(str(x))
            except ValueError:
                return False
            else:
                return True
        else:
            return True

    # noinspection PyUnusedLocal
    @classmethod
    def mod_to_num(cls, x):
        if cls.is_valid_numeric(x):
            try:
                a = float(str(x))
            except ValueError:
                return int(str(x))
            else:
                return a

    @classmethod
    def is_user_abort(cls, x):
        return True if x in cls.aborts else False

    @classmethod
    def is_streamlined(cls, x):
        return True if x in cls.yeses else False

    @staticmethod
    def mod_to_lower(x):
        return x.lower()

    @classmethod
    def begin(cls):
        """
        Starts the user input prompt and orchestrates the flow of it
        :return:
        """
        cls.print_header()
        if not cls.input_default_or_custom():
            cls.input_currency()
        else:
            Currency.use_default_currency()
        cls.print_footer()

    @classmethod
    def print_header(cls):
        """
        prints a header on the prompt
        :return:
        """
        print("*******************************************")
        print("Welcome to my coin combinator!")
        print("*******************************************")

    @classmethod
    def print_footer(cls):
        """
        prints a footer/summary on the prompt
        :return:
        """
        print("*******************************************")
        print("Thank you for your input.")
        print("*******************************************")
        print("Now printing combinations:")

    @classmethod
    def input_currency(cls):
        """
        prompt for getting user input on how to define a set of currency
        one unit of currency at a time.
        :return:
        """
        is_input_complete = False
        coin_input = list()
        i = 0
        input_do_another = None
        # Loop through until all coins have been defined
        while not is_input_complete:
            is_input_complete = True
            # Define coin
            print("Let's define a coin. We need a name and a value.")
            coin_input.append([])
            coin_input[i].append(cls.prompt_for_input("What is this new coin's name: ", cls.is_valid_alpha,
                                                         cls.mod_to_lower))
            coin_input[i].append(cls.prompt_for_input(
                    "how many %s coins will it take to reach the target value? " % coin_input[i][0],
                    cls.is_valid_numeric, cls.mod_to_num))
            # check for repeat
            input_do_another = cls.prompt_for_input("Define another? ", cls.is_valid_control, cls.mod_to_lower)
            i += 1
            if input_do_another in cls.yeses:
                is_input_complete = False
        Currency.define_by_list(coin_input)
        Currency.process_defined_values()

    @classmethod
    def input_default_or_custom(cls):
        """
        get user input for default currency or define a custom set.
         sets flags appropriately.
        :return:
        """

        input_default_currency = cls.prompt_for_input(
                "%s %s" % ("Would you like to use the default currency? ", cls.yes_no_str), cls.is_valid_control,
                cls.mod_to_lower)
        if cls.is_user_abort(input_default_currency):
            Control.user_exit()
        Control.is_streamlined = cls.is_streamlined(input_default_currency)
        return Control.is_streamlined

    @classmethod
    def prompt_for_input(cls, prompt, validator, modifier):
        """
        Gets user input from prompt and modifies it and validates it via lambda args
        :param prompt: leading prompt for user input
        :param validator: lambda for validating
        :param modifier: lambda for modifying
        :return: output of input()
        """
        output = modifier(input(prompt))
        while not validator(output):
            print("Invalid input. Please try again.")
            output = modifier(input(prompt))
        return str(output)

    @classmethod
    def input_command_line_args(cls):
        pass
        # TODO implement
