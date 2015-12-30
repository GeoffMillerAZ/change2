import sys

from Errors import ErrorCodes, ErrorMessages


class Control:
    """

    """
    is_streamlined = False
    target = None
    r_target = None

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