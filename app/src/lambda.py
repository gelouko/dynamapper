import logging
import os

logging.getLogger().setLevel(os.getenv("LOG_LEVEL", logging.INFO))


def lambda_handler(event, context):
    logging.info("Hello World!")
