from src.exception import CustomException
from src.logger import logging
import sys

def divide(a, b):
    try:
        logging.info("Attempting division operation")
        result = a / b
        logging.info(f"Division successful: result = {result}")
        return result
    except Exception as e:
        logging.error("Division failed")
        raise CustomException(e, sys)
divide(1,0)