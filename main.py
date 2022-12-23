import logging
import logging.config
from config import Configs
from purchasing.utilities import Utilities as Util


def main():
    logger.info("from main")
    logger.info(configs.is_prod)
    logger.info(configs.podio_client_id)


def get_logger():
    """returns a configure logger"""
    log_format = "%(asctime)s | %(levelname)s: %(message)s"

    # Create and configure logger
    logging.basicConfig(filename="app.log", format=log_format)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(log_format))

    # Creating an object
    logger = logging.getLogger()

    logger.addHandler(console_handler)

    logger.setLevel(logging.DEBUG)

    return logger


if __name__ == "__main__":
    is_prod = True

    global logger
    logger = get_logger()

    logger.info("Starting...")

    # loading configs
    logger.info("loading configs")

    global configs
    configs = Configs(is_prod)

    main()

    try:
        # main()
        pass
    except KeyboardInterrupt:
        logger.error("Something went wrong...\n\n")
        exit()
    finally:
        logger.info("Exiting...\n\n")
