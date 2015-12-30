from Control import Control
from Currency import Currency


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
            print(Currency.printer(solution))
            Currency.num_solutions += 1
            return 1
        if (cointh + 1) == len(Currency.r_values):
            if remain % Currency.sorted_val(cointh) == 0:
                solution.append((int(remain / Currency.sorted_val(cointh)), Currency.get_coin_name(Currency.sorted_val(cointh))))
                print(Currency.printer(solution))
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