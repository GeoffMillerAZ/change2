# Author Geoff Miller
# Date: 12-26-15
# Currency Problem


from enum import IntEnum


class ErrorCodes(IntEnum):
    """
    Stores the integer error codes. Use ErrorMessage for human code messages
    """
    R_SUCCESS = 0
    E_FAILURE = 1
    E_USER_EXIT = 2
    E_UNEXPECTED_TERMINATION = 3
    E_ZERO = 4


class ErrorMessages:
    """
    Stores the human readable error messages
    """
    errors = [
        "General success",
        "General failure",
        "User initiated exit",
        "An error has caused the program to exit",
        "Zero is not a valid value for currency value!"
    ]

    @classmethod
    def verbose(cls, num):
        """For returning the verbose, human-readable error code
        :param num: the error code number
        :return:
        """
        return str(cls.errors[num])
