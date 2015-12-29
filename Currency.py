# Author Geoff Miller
# Date: 12-26-15
# Currency Problem


from Errors import ErrorCodes
from Errors import ErrorMessages
import operator


class Currency:
    """
    Defines a currency set
    """
    # number of solutions
    num_solutions = 0
    solutions = {}
    # currency names
    names = {}
    # currency values
    values = {}
    # adjusted currency values.
    r_values = {}
    # list of defined currency names sorted by value
    s_values = []
    # bool for keeping track if the amounts need adjusted
    is_adjusted = False

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
