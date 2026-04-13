import sys
from src.logger import logging


def error_message_detail(error, error_detail: sys) -> str:
    """
    Extracts a rich error message from the current exception context.

    Parameters:
        error        : The exception object caught in the except block
        error_detail : The sys module, passed in to access exc_info()

    Returns:
        A formatted string with script name, line number, and error message
    """
    # exc_info() returns (type, value, traceback). We only need the traceback.
    _, _, exc_tb = error_detail.exc_info()

    # Navigate the traceback object to find the source file and line number
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = (
        "Error occurred in Python script: [{0}] "
        "at line number: [{1}] "
        "with message: [{2}]"
    ).format(file_name, exc_tb.tb_lineno, str(error))

    return error_message


class CustomException(Exception):
    """
    A project-wide custom exception that enriches error messages
    with file name and line number context.
    """

    def __init__(self, error_message, error_detail: sys):
        # Initialise the parent Exception class with the raw message
        super().__init__(error_message)

        # Enrich the message using our helper function
        self.error_message = error_message_detail(
            error=error_message,
            error_detail=error_detail
        )

    def __str__(self):
        # When the exception is printed, show the enriched message
        return self.error_message
    
# Add temporarily to exception.py for testing
if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.info(CustomException(e, sys))
        raise CustomException(e, sys)