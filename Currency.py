# Author Geoff Miller
# Date: 12-26-15
# Currency Problem
import operator

from Control import Control
from Errors import ErrorCodes


class Currency:
    """
    Defines a currency set
    """
    # num of solutions
    num_solutions = 0
    # currency names
    names = {}
    # currency values
    values = {}
    # number of coins to hit target
    r_values = {}
    # list of defined currency names sorted by value
    s_values = []
    # bool for keeping track if the amounts need adjusted
    is_adjusted = False
    max_name_len = 0

    @staticmethod
    def use_default_currency():
        Control.target = 100
        Currency.define("quarter", 25)
        Currency.define("dime", 10)
        Currency.define("nickle", 5)
        Currency.define("penny", 1)
        Currency.process_defined_values()

        # Control.target = 1500
        # Currency.define("coin", 1000)
        # Currency.define("arrowhead", 500)
        # Currency.define("button", 10)
        # Currency.process_defined_values()

    @classmethod
    def get_coin_name(cls, val):
        """
        Prints only the name of the specified currency unit
        :param val: val of the unit name to print
        :return:
        """
        # TODO forgot where i was going with this...
        return cls.names[val]

    @classmethod
    def get_coin_val(cls, name):
        """
        returns the value of the named coin in the currency set
        :param name: name of coin
        :return: value of coin
        """
        return cls.values[name]

    @classmethod
    def define(cls, name, val):
        """Defines a unit of currency with a name and value (AKA "coin")
        :param val: value of the unit being defined
        :param name: label of the unit being defined
        :return:
        """
        cls.values[name] = val
        cls.names[val] = name
        return ErrorCodes.R_SUCCESS

    @classmethod
    def define_by_list(cls, list):
        target = None
        nums = []
        r_nums = []
        vals = []
        names = []
        has_float = False
        for coin in list:
            if isinstance(coin[1], float):
                has_float = True
                break
        if has_float:
            for coin in list:
                if has_float:
                    nums.append(float(coin[1]))
                else:
                    nums.append(int(coin[1]))
                names.append(str(coin[0]))
        else:
            for coin in list:
                nums.append(float(coin[1]))
                names.append(str(coin[0]))

        target = max(nums)
        r_nums = nums[:]

        while has_float:
            has_float = False
            target *= 10
            for coin in r_nums:
                coin *= 10
                if not has_float:
                    has_float = not coin.is_integer()

        Control.target = target

        for i, coin in enumerate(r_nums):
            if r_nums[i] == 0:
                Control.error_exit(ErrorCodes.E_ZERO)
            Currency.define(names[i], (target / r_nums[i]))

    @classmethod
    def process_defined_values(cls):
        """
        checks for values that are not integers and adjusts values
        so that all numbers will work with integer arithmetic

        also performs other utility tasks on finalized currency set
        :return:
        """
        if not cls.is_adjusted:
            cls.s_values = sorted(cls.values.items(), key=operator.itemgetter(1), reverse=True)
            cls.r_values = cls.values
            # TODO revisit r_values
            cls.is_adjusted = True
        return ErrorCodes.R_SUCCESS

    @classmethod
    def sorted_val(cls, val):
        """
        :param val: value
        :return: return the value of the nth valued coin
        """
        return cls.s_values[val][1]

    @classmethod
    def printer(cls, list):
        output = ""
        for coin in list:
            plural = "s"
            if coin[0] == 1:
                plural = ""
            output += " | %s %-s%+s" % (str(coin[0]).ljust(3), str(coin[1]), plural.ljust(2))
        return output
