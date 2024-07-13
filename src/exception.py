import sys
import logging
from logger import logging  # Assuming logger.py has been properly set up

def error_message_detail(error, exc_tb):
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in Python script [{file_name}] at line number [{line_number}] with message: {str(error)}"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, exc_tb):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, exc_tb)

    def __str__(self):
        return self.error_message

